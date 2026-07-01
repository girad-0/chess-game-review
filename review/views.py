from django.shortcuts import render, redirect, get_object_or_404
from .forms import PGNUploadForm
from .models import Review
from .move_parser import parse_pgn
import io


def home(request):

    if request.method == "POST":

        form = PGNUploadForm(request.POST, request.FILES)

        if form.is_valid():

            uploaded_file = request.FILES["pgn_file"]

            # Read uploaded file as text
            pgn_text = uploaded_file.read().decode("utf-8")

            # Create a text stream for python-chess
            review_data = parse_pgn(io.StringIO(pgn_text))

            # Save everything
            Review.objects.create(
                white_player=review_data["white"],
                black_player=review_data["black"],
                event=review_data["event"],
                date=review_data["date"],
                result=review_data["result"],
                pgn=pgn_text,
            )

            return redirect("home")

    else:
        form = PGNUploadForm()

    reviews = Review.objects.all().order_by("-created_at")

    return render(
        request,
        "review/home.html",
        {
            "form": form,
            "reviews": reviews,
        },
    )


def review_page(request, review_id):

    review = get_object_or_404(Review, id=review_id)

    review_data = parse_pgn(io.StringIO(review.pgn))

    return render(
        request,
        "review/review_page.html",
        {
            "review": review,
            "review_data": review_data,
        },
    )
# Book Recommendation System

This is a book recommendation system implemented using Django and machine learning. It suggests books similar to the one provided by the user.

## Prerequisites

- Python 3.x
- Django
- NumPy
- pandas

## Installation

1. Clone the repository:


2. Install the required dependencies:


## Usage

1. Run the Django server:


2. Access the application through a web browser at `http://localhost:8000`.

3. Enter the name of a book in the input field and submit the form.

4. The system will recommend similar books based on the provided input.

## Files

- `model.pkl`: Pickled machine learning model used for recommendation.
- `books_name.pkl`: Pickled list of book names.
- `final_rating.pkl`: Pickled dataframe containing book ratings and other details.
- `book_pivot.pkl`: Pickled pivot table for books.

## Components

- `views.py`: Contains Django views for rendering HTML templates and handling requests.
- `urls.py`: URL configurations for the Django application.
- `models.py`: Contains models for data handling (if any).
- `templates/`: Directory containing HTML templates for the web application.
- `static/`: Directory containing static files like CSS, JavaScript, and images.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project was inspired by the desire to create a personalized book recommendation system.
- Thanks to the Django and machine learning communities for their valuable resources and documentation.


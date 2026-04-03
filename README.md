# MB Django Project

This is a Django-based web application for managing blog posts and pages.

## Features
- Blog post creation, editing, and deletion
- User authentication (admin panel)
- Dashboard and static pages
- API endpoints for analytics

## Getting Started

### Prerequisites
- Python 3.8+
- pip
- (Recommended) Virtual environment

### Setup
1. Clone the repository:
	```sh
	git clone <your-repo-url>
	cd mb
	```
2. Create and activate a virtual environment:
	```sh
	python -m venv .venv
	# On Windows
	.venv\Scripts\activate
	# On Mac/Linux
	source .venv/bin/activate
	```
3. Install dependencies:
	```sh
	pip install -r requirements.txt
	```
4. Run migrations:
	```sh
	python manage.py migrate
	```
5. Create a superuser:
	```sh
	python manage.py createsuperuser
	```
6. Start the development server:
	```sh
	python manage.py runserver
	```

Visit http://127.0.0.1:8000/ in your browser.

## Deployment
This project can be deployed to [Render](https://render.com/). See Render's Django deployment guide for details.

## License
MIT
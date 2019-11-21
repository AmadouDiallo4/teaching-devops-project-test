
all: test

test:
	pipenv run pytest tests/test_control.py
	pipenv run pytest --hosts=s0.infra tests/test_lb.py
	pipenv run pytest --hosts=s1.infra tests/test_app.py
	pipenv run pytest --hosts=s2.infra tests/test_app.py
	# pipenv run pytest --hosts=s3.infra tests/test_s3.py
	# pipenv run pytest --hosts=s4.infra tests/test_s4.py


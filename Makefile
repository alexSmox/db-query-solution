dump:
	docker compose exec postgres pg_dump -U username database > dump.sql

restore:
	docker compose exec -T postgres psql -U username -d database < dump.sql

solution1:
	docker compose run --rm alembic python solution1.py

solution2:
	docker compose run --rm alembic python solution2.py

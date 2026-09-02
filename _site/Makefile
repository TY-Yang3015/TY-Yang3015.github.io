.PHONY: posts posts-check posts-pdf build serve

posts:
	python3 scripts/build_tex_posts.py

posts-check:
	python3 scripts/build_tex_posts.py --check

posts-pdf:
	python3 scripts/build_tex_posts.py --pdf

build: posts
	bundle exec jekyll build

serve: posts
	bundle exec jekyll serve

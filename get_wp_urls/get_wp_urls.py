import requests

API_URL = "https://ki-hi-ro.com/wp-json/wp/v2/posts"
OUTPUT_FILE = "wp_article_urls.txt"
START_DATE = "2026-05-27T00:00:00"


def fetch_all_post_urls() -> list[str]:
    urls = []
    page = 1

    while True:
        response = requests.get(
            API_URL,
            params={
                "status": "publish",
                "after": START_DATE,
                "per_page": 100,
                "page": page,
                "orderby": "date",
                "order": "desc",
                "_fields": "link",
            },
            timeout=30,
        )
        response.raise_for_status()

        posts = response.json()
        urls.extend(post["link"] for post in posts)

        total_pages = int(
            response.headers.get("X-WP-TotalPages", "1")
        )

        print(f"{page}/{total_pages}ページを取得しました")

        if page >= total_pages:
            break

        page += 1

    return urls


def save_urls(urls: list[str]) -> None:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write("\n".join(urls))

    print(f"{len(urls)}件のURLを {OUTPUT_FILE} に保存しました")


if __name__ == "__main__":
    article_urls = fetch_all_post_urls()
    save_urls(article_urls)
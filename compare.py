from urllib.parse import urlparse
import re

def read_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file.readlines()]
    return urls

def remove_duplicates(urls):
    unique_urls = set(urls)
    return unique_urls

def remove_duplicates_from_another_set(urls, other_urls):
    unique_urls = set(urls)
    other_unique_urls = set(other_urls)
    unique_urls -= other_unique_urls
    return unique_urls

def remove_common_urls(urls, other_urls):
    unique_urls = set(urls)
    common_urls = unique_urls.intersection(other_urls)
    return common_urls

def remove_non_common_urls(urls, common_urls):
    non_common_urls = set(urls) - set(common_urls)
    return non_common_urls

def extract_domains(urls):
    domains = set()
    for url in urls:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        domains.add(domain)
    return domains

def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for item in data:
            file.write("%s\n" % item)

def remove_urls_with_keywords(urls, keywords):
    # Define the regex pattern for URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')

    # Define a function to check if a URL contains any of the keywords
    def contains_keyword(url):
        for keyword in keywords:
            if keyword.lower() in url.lower():
                return True
        return False

    # Remove URLs containing keywords
    cleaned_urls = [url for url in urls if not contains_keyword(url)]

    return cleaned_urls

def main():
    urls_file_path = 'urls.txt'  # Path to the text file containing URLs
    other_urls_file_path = 'other_urls.txt'  # Path to the text file containing other URLs
    output_file_path = 'output.txt'  # Path to the output text file

    # Read URLs from files
    urls = read_urls_from_file(urls_file_path)
    other_urls = read_urls_from_file(other_urls_file_path)

    # Step 1: Remove duplicates
    unique_urls = remove_duplicates(urls)
    step1_output = ["Step 1: Remove duplicates (Count: {})".format(len(unique_urls)), ''] + list(unique_urls)

    # Step 2: Keep only common URLs
    common_urls = remove_common_urls(unique_urls, other_urls)
    step2_output = ["Step 2: Common URLs (Count: {})".format(len(common_urls)), ''] + list(common_urls)

    # Step 3: Remove common URLs from the list of removed duplicates
    unique_common_urls = remove_duplicates_from_another_set(unique_urls, common_urls)
    step3_output = ["Step 3: Unique URLs (Count: {})".format(len(unique_common_urls)), ''] + list(unique_common_urls)

    # Step 4: Extract domains from step 2 and step 3 URLs
    step_4_urls = common_urls.union(unique_common_urls)
    step4_output = ["Step 4: Domains from Step 2 and Step 3 URLs:", ''] + list(extract_domains(step_4_urls))

    # Step 5: Remove URLs containing excluded keywords
    excluded_keywords = ['vidio',
                         'tiktok',
                         'instagram',
                         'twitter',
                         'watch.plex.tv',
                         'youtube',
                         'idntimes',
                         'wattpad',
                         'liputan6',
                         'accounts.google',
                         "wiki",
                         "imdb",
                         "news",
                         "netflix",
                         "hotstar",
                         "amazon prime",
                         "zee5",
                         "disney",
                         "article",
                         "bookmyshow",
                         "rottentomatoes",
                         "justwatch",
                         "sarkarisresults",
                         "id.linkedin.com",
                         "support.google.com",
                         "sound.cloud",
                         "digstraksi.com",
                         "majalengka.pikiran-rakyat.com",
                         "soundcloud.com",
                         "depok.hallo.id",
                         "filmonizirani.net",
                         "www.kompasiana.com",
                         "www.viv.co.id",
                         "www.mengerti.id",
                         "www.amazon.com",
                         "trakt.tv/movies",
                         "www.layar.id",
                         "trakt.tv",
                         "shopee.co.id",
                         "www.themoviedb.org",
                         "www.moviefone.com",
                         "rebahinxxi.pro",
                         "telemetr.io",
                         "www.dailysia.com",
                         "shopee.co.id",
                         "www.moviefone.com/",
                         "www.google.com"]
    cleaned_urls = remove_urls_with_keywords(step_4_urls, excluded_keywords)
    step5_output = ["Step 5: URLs after removing excluded keywords:", ''] + list(cleaned_urls)

    # Write all outputs to the output file
    output_data = step1_output + [''] * 2 + step2_output + [''] * 2 + step3_output + [''] * 2 + step4_output + [''] * 2 + step5_output
    write_to_file(output_file_path, output_data)

if __name__ == "__main__":
    main()

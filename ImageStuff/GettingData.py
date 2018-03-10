import GoogleApi

def dataOnImage(url, min_label_score = 0.0, limit_of_urls = -1):
    """
    dict file structure:
        "labels": [(labe_name, score)]
        "urls_to_similar_sides": ["url"]
    """

    information = GoogleApi.annotate(url)
    dict = {"labels": [],
            "urls_to_similar_sides": []}

    for entity in information.web_entities:
        if entity.score >= min_label_score:
            dict["labels"] += [(entity.description, entity.score)]

    if (limit_of_urls == -1):
        for page in information.pages_with_matching_images:
            dict["urls_to_similar_sides"] += [page.url]
    else:
        for page in information.pages_with_matching_images[:limit_of_urls]:
            dict["urls_to_similar_sides"] += [page.url]
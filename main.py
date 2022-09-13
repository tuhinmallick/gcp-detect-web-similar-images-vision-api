def detect_web(path):
    """Detects web annotations given an image."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.web_detection(image=image)
    annotations = response.web_detection

    images = []
    description = ""
    if annotations.best_guess_labels:
        for label in annotations.best_guess_labels:
            description = '\nBest guess label: {}'.format(label.label)

    if annotations.pages_with_matching_images:
        description = '\n{} Pages with matching images found:'.format(
            len(annotations.pages_with_matching_images))

        for page in annotations.pages_with_matching_images:
            description += '\n\tPage url   : {}\n'.format(page.url)

            if page.full_matching_images:
                description += '\t{} Full Matches found: \n'.format(
                       len(page.full_matching_images))

                for image in page.full_matching_images:
                    description += '\t\tImage url  : {}\n'.format(image.url)

            if page.partial_matching_images:
                description += '\t{} Partial Matches found: \n'.format(
                       len(page.partial_matching_images))

                for image in page.partial_matching_images:
                    description += '\t\tImage url  : {}\n'.format(image.url)

    if annotations.web_entities:
        # print('\n{} Web entities found: '.format(
        #     len(annotations.web_entities)))
        description += f'\n{len(annotations.web_entities)} Web entities found: '

        for entity in annotations.web_entities:
            description += '\n\tScore      : {}\n'.format(entity.score)
            description += u'\tDescription: {}\n'.format(entity.description)
            # print('\n\tScore      : {}'.format(entity.score))
            # print(u'\tDescription: {}'.format(entity.description))

    if annotations.visually_similar_images:
        description += '\n{} visually similar images found:\n'.format(
            len(annotations.visually_similar_images))

        for image in annotations.visually_similar_images:
            description += '\tImage url    : {}\n'.format(image.url)
            images.append(image.url)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    print(len(images))
    images = filter(lambda x:x.startswith(("http", "https")), images)
    return images, description
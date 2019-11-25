import os

def load_hyponyms(file_path):
	hyponyms_of_persons = set()

	with open(file_path) as infile:
		for line in infile:
			line = line.strip()
			line = line.replace("<", "").replace(">", "")
			hyponyms_of_persons.add(line)
	return hyponyms_of_persons


def is_person_image(image_tags_split, hyponyms_of_persons):
	if len(image_tags_split) == 1 and image_tags_split[0] in hyponyms_of_persons:
		return True

	count_person_tags = 0
	for tag in image_tags_split:
		if tag == 'wikicat_People_by_name':
			continue

		if tag in hyponyms_of_persons:
			count_person_tags += 1

	return True if count_person_tags >= 2 else False


def flatten_all_tags(image_tags):
	image_tags = image_tags.replace("{", "<").replace("}", ">")
	image_tags_split = image_tags[1:len(image_tags) - 1].split(">, <")
	image_tags_split = [tag.replace("<", "").replace(">", "").replace(
		"[", "").replace("]", "") for tag in image_tags_split if tag != '<>']

	return image_tags_split


def append_line_to_file(line, filename):
	with open(filename, "a+") as f:
		f.write(line)


def parse_str_to_tags(image_tags_str):
	image_tags_split = image_tags_str[2:len(image_tags_str) - 2].split(">, <")

	return image_tags_split

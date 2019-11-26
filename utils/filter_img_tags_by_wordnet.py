import sys
import os.path
import IOUtility


def import_hyponyms(file_path):
	with open(file_path) as f:
		hyponyms = f.readlines()
		hyponyms = [a_hyponym.strip()[1:-1] for a_hyponym in hyponyms]
	return hyponyms


def main():
	if len(sys.argv) != 2:
		print("Should have two arguments!")
		return

	# check if the input file exist
	if not os.path.exists(sys.argv[1]):
		print("The second argument should be the input file of all the hyponyms of a wordnet")
		return

	# extract the valid file name
	output_file_name = "results_" + os.path.splitext(os.path.basename(sys.argv[1]))[0]+".tsv"
	# remove this file if existed
	try:
		os.remove(output_file_name)
	except OSError:
		pass


	# import all the hyponyms
	hyponyms = import_hyponyms(sys.argv[1])

	counter = 0

	# start filtering
	with open("./img_tags_locations.tsv") as f:
		for line in f:
			splited_line = line.strip().split("\t")
			tags = IOUtility.flatten_all_tags(splited_line[2])
			for a_tag in tags:
				if a_tag in hyponyms:
					IOUtility.append_line_to_file(line, output_file_name)
					counter += 1
					break
	print("{} images found with this wordnet synsets".format(counter))


if __name__ == "__main__":
	main()
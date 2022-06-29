#!/usr/bin/env python
import glob
import os
from ast import literal_eval

# Reference URL => https://longqian.me/2017/02/09/github-jekyll-tag/
post_dir = '_posts/'
tag_dir = 'tags/'
filenames = glob.glob(post_dir + '*md')

if not os.path.exists(tag_dir):
    os.makedirs(tag_dir)

total_tags = []

for filename in filenames:
	f = open(filename, 'rt', encoding='utf-8')
	flag = False

	for l in f:

		if (flag):
			c_matter = l.strip().split(':')

			if (c_matter[0] == 'tags'):

				if (c_matter[1].strip().startswith('[')):
					clean_tags = ''.join(c for c in c_matter[1] if c not in '[]')
					list_tags = map(str.strip, clean_tags.split(','))
					total_tags.extend(list_tags)

				else:
					list_tags = map(str.strip, c_matter[1].strip().split())
					total_tags.extend(list_tags)

				flag = False

				break

		if (l.strip() == "---"):

			if (flag):
				flag = False

				break

			else:
				flag = True

	f.close()

total_tags = set(total_tags)
pre_tags = glob.glob(tag_dir + "*.md")

for tag in pre_tags:
	os.remove(tag)

for tag in total_tags:
	tag_filename = tag_dir + tag.replace(' ', '_') + '.md'
	f = open(tag_filename, 'at')
	write_str = f'---\nlayout: tag\ntitle: \"Selected: {tag}\"\npermalink: tags/{tag}\npermalink_name: tags/{tag}\n\ntags: {tag}\n---\n'
	f.write(write_str)
	f.close()

print("Tags generated, count", total_tags.__len__())

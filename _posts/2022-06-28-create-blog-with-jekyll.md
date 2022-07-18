---
layout: post
title: 지킬테마 블로그
post-title: 지킬테마 블로그
date: 2022-06-28 10:59:00 +0900
# last_modified_at:
permalink: /blog/jekyll_themes.html
permalink_name: /blog/jekyll_themes
category: blog
description: 깃허브 블로그는 자유도가 높기 때문에 웹서버를 직접 수정할 일이 생각보다 많습니다. 이 포스트를 통해 제가 개인적으로 원하는 형태의 블로그를 만들기 위해 웹서버의 수정사항에 관해 기록합니다.
tags: [liquid, html, jekyll]

detail_image: /assets/images/thumb/octocat_jekyll.jpg
---

# 시작하며

&nbsp; 첫 포스트가 하필 **지킬테마 블로그**인 이유는 원래는 이미 제가 구현한 작업물에 대한 포스팅을 하려했는데, 블로그를 꾸준히 관리하기 위해서는 블로그 자체가 제 마음에 들어야하기 때문에 무척이나 중요한 작업이라 생각이 들게 되었습니다. 제 관심분야와 멀기 때문에 취업에 있어서 중요도가 높아보이지는 않지만 마음에 들지 않는 블로그는 한번 체험해보는 식으로 끝날 가능성이 높아서 저에게 **블로그 관리** 자체의 문제이므로 정말 중요합니다.

&nbsp; 작업 환경은 Linux-Ubuntu-20.04 이기 때문에 만약 Windows에서 작업한다면 bash를 통해 진행하시면 됩니다. 아마 Windows에서 [``git bash``](https://git-scm.com/downloads) 를 다운로드 해서 bash를 사용할 수 있을 것입니다. 만약 terminal 환경을 사용해본 경험이 없다면 내용을 따라가기 힘들 수 있습니다.

&nbsp; 마지막으로 이 [블로그 소스](https://github.com/Kuiper68/Kuiper68.github.io)는 모든 스크립트를 제 습관에 맞게 들여쓰기를 적용해놓았기 때문에 원본소스와 비교해서 보려면 다소 불편할 수 있습니다.
<br>

# 지킬테마 선택

&nbsp; 이 포스트를 보고 처음 블로그를 시작하고 있다면 제가 선택한 [``jekyll-shell-theme``](https://github.com/tareqdandachi/jekyll-shell-theme "a light-weight customizable one-column jekyll theme") 를 선택하셔도 괜찮으나 테마 선택은 개개인의 취향을 많이 타고 블로그 스타일이 마음에 들지 않으면 꾸준히 하기 힘들기 때문에(물론 저만의 생각일 수도 있지만...) [``jekyllthemes.org``](http://jekyllthemes.org/) 에서 최대한 마음에 드는 스타일을 선택하시기를 추천드립니다.
<br>

<center>
  <img src="/assets/images/content/github_repo.png" width="90%">
</center>

&nbsp; 테마를 선택하셨다면 해당 테마의 깃허브 저장소에서 **Fork**를 통해 나의 저장소로 소스를 복사합니다. 깃허브 저장소의 오른쪽 상단에 **Fork**버튼이 있습니다. 눌러서 저장소 복사를 진행하시면 됩니다. 저장소의 이름은 *(user_id).github.io* 로 설정하시면 됩니다.

&nbsp; 마지막으로 테마 소스 수정을 하기위해 로컬로 저장소를 복제합니다. terminal 환경에서 ``git clone`` 명령어를 사용하면 간단하게 복제됩니다. 저장소에서 code 버튼을 눌러 저장소의 URL을 ``git clone`` 뒤에 붙여 실행합니다.

```bash
git clone https://github.com/(user_id)/(user_id).github.io.git
```
<br>

# 테마 설정 초기화

&nbsp; [``jekyll-shell-theme``](https://github.com/tareqdandachi/jekyll-shell-theme "a light-weight customizable one-column jekyll theme") 테마가 깔끔하고 취향에 맞아 선택했지만 테마 자체의 기능이 많지는 않기 때문에 직접 커스터마이징 해야할 부분이 상당수 존재합니다. 우선 포스트를 작성하고 난 뒤 수정할 때 **최종 수정일자**가 표시되면 좋을 것 같습니다. ``/`` (root) 디렉토리에 있는 [``/Gemfile``](https://github.com/tareqdandachi/jekyll-shell-theme/blob/master/Gemfile) 에 ``gem jekyll-last-modified-at``을 추가합니다.

```shell
# Gemfile
...

group :jekyll_plugins do
  gem 'jemoji'
  gem 'jekyll-last-modified-at' # 추가
end
```
<br>

&nbsp; 그리고 ``/`` 디렉토리에 있는 [``/_config.yml``](https://github.com/tareqdandachi/jekyll-shell-theme/blob/master/_config.yml) 을 수정합니다. 우선 아래의 내용만 수정하면 될 것입니다. 테마에 따라 내용이 조금씩 다를 수 있습니다.

```yml
# _config.yml
title: "implementation_challenge"
tagline: "A jekyll theme that looks like a shell/terminal"
description: "이론적인 내용들을 직접 구현해보고 정리하기 위해 만든 사이트입니다."
github_username: "kuiper68"
baseurl: ""
url: "https://kuiper68.github.io"
theme: jekyll-shell-theme

plugins:
...

```
<br>

&nbsp; 이제 terminal 환경에서 ``bundle install`` 명령을 실행해서 웹서버의 변경사항을 적용합니다. 그리고 ``bundle exec jekyll serve`` 를 터미널에 입력해서 웹이 정상적으로 **작동**되는지 확인합니다. 명령어를 실행함으로써 [로컬호스트IP](http://127.0.0.1:4000/ "http://127.0.0.1:4000/")로 만들어진 웹서버에 **접근**할수있습니다.

```shell
bundle install
bundle exec jekyll serve
```
<br>

&nbsp; 문제없이 동작한다면 웹 페이지의 **메인**을 수정합니다. ``/`` 디렉토리의 [``/index.md``](https://github.com/tareqdandachi/jekyll-shell-theme/blob/master/index.md) 를 자신의 컨셉에 맞게 수정해주시면 됩니다. 이때 ``detail_image`` 는 메인 타이틀로 설정될 이미지이기 때문에 원하는 이미지를 자유롭게 다운받아 사용하시면 됩니다. 아래 코드블록에서 **front matter** 상단의 ``layout: home`` 은 ``/_layouts/home.html`` 을 페이지의 템플릿으로 활용한다는 뜻으로 생각하시면 될 것입니다.

```markdown
---
layout: home
permalink: /
permalink_name: /home
title: home

detail_image: /assets/images/main/site_main_title_purple.png

---
...
```
<br>

&nbsp; ``/index.md`` 를 수정해 보았으면 다음 웹페이지의 생성도 수월할 것입니다. 다음은 ``/about.md`` 를 생성할 것입니다. 이 페이지에는 자신에 대한 공유 가능한 정보를 열거합니다. 내용은 천천히 작성해도 상관없으니 우선 front matter 만 완성합니다.

```markdown
---
layout: home
permalink: /about
permalink_name: /about
title: about

detail_image: /assets/images/main/site_main_title_pink.png

---

# About me
---
...
```
<br>

&nbsp; 페이지 생성을 마쳤으면 ``/_config.yml`` 의 ``header_pages`` 에 ``/about.md`` 를 추가합니다. 이 부분은 테마마다 다를 수 있기 때문에 **상단바(header)**에 메뉴를 설정하는 곳이 어디인지 찾아서 적용하면 될 것 같습니다.

```yml
# _config.yml
...
header_pages:
  - index.md
  # - read-me.md
  # - preview.md
  - about.md
...
```
<br>

&nbsp; 다음은 웹의 콘텐츠(포스트)를 보여줄 페이지 메뉴를 생성할 것입니다. 저의 경우는 ``/blog.md``로 페이지를 생성하려 합니다. 하지만 페이지를 생성하기 전에 포스트들을 어떻게 보여줄 것인가에 대해 정의를 해야합니다. 또한 포스트들에 ``tag`` 를 달아 포스트들을 정리하고 싶었습니다. ``liquid`` 문법을 다뤄 보았으면 내용을 이해하기 수월할 것 입니다. 우선 ``blog`` 페이지의 레이아웃 부터 다루겠습니다. 우선 ``/_layouts/blog.html``을 생성하고 다음과 같이 작성합니다. 문법이 난해하게 느껴질 수 있으니 주석으로 번호를 달아 내용을 정리하였습니다.

```html
{% raw %}---
layout: default <!-- 1 -->
---

{%- if page.detail_image -%}
  <img class="home_header" src="{{ page.detail_image }}"> <!-- 2 -->

{%- endif -%}

{{ content }} <!-- 3 -->
<ul>
  {% assign lastpost = site.posts | last %} <!-- 4 -->

  {% for post in site.posts %}

    {% if post.category == "blog" %}
      <div class="post-viewer"> <!-- 5 -->
        <div class="post-content"> <!-- 6 -->
          <a href="{{ post.permalink }}"> <!-- 7 -->
            <span><font size=4>{{post.title}}</font></span> <!-- 8 -->
		  </a>
          <br>

		  {% assign date_split = post.date | split: " " %} <!-- 9 -->
		  <i>
		    created: {{ date_split[0] }} <!-- 10 -->
		  </i>
		  <br>
		  tags:

		  {% for tag in post.tags %}
		    <a href="/tags/{{ tag }}"> <!-- 11 -->
		      <code>
			    <nobr>{{ tag }}</nobr> <!-- 12 -->
		      </code>
		    </a>
		    &nbsp;

		  {% endfor %}

		  <br><br>

          <div class="post-desc">{{post.description}}</div> <!-- 13 -->

        </div>
        <div class="post-thumbnail"> <!-- 14 -->
          <a href="{{ post.permalink }}">
            <img class="thumbnail"; src="{{ post.detail_image }}"> <!-- 15 -->
          </a>
        </div>
      </div>
    {% endif %}

    {% if post == lastpost %}

      {% break %} <!-- 16 -->

    {% endif %}

	<hr> <!-- 17 -->

  {% endfor %}

</ul>{% endraw %}
```

1. /_layouts/default.html 을 레이아웃으로 사용합니다
2. page에 detail_image라는 테그를 front matter에 정의했다면 /assets/css/main.scss 에 정의된 home_header 라는 스타일로 이미지를 출력합니다
3. 페이지 ``/blog.md`` 에 작성된 콘텐츠를 출력합니다
4. ``<hr>`` 태그로 포스트 사이에 격자를 두려 하는데 마지막 격자가 생성되고 끝나면 개인적으로 약간 불편해서 마지막 포스트가 무엇인지를 미리 할당해서 마지막 for 루프가 실행될 때 break 를 통해 ``<hr>``이 생성되기 전에 빠져나오기 위해 변수를 할당했습니다 (16, 17 참고)
5. /assets/css/main.scss 에 제가 정의한 스타일입니다
6. 5와 같습니다
7. 5와 같습니다
8. 링크가 걸린 포스트의 타이틀을 출력합니다
9. 포스트의 date에서 날짜만 가져오기 위해 할당했습니다
10. 포스트가 생성된 날짜를 출력합니다
11. 태그를 클릭하면 해당 태그를 보여주는 페이지로 이동하기 위해 링크를 달아줍니다
12. for 루프를 통해 태그를 하나 하나씩 출력합니다
13. 포스트에 대한 간단한 설명을 출력합니다
14. 5와 같습니다
15. /assets/css/main.scss 에 제가 정의한 스타일이며 썸네일도 마찬가지로 링크를 걸어 포스트로 이동할 수 있도록 합니다
16. 마지막 포스트를 만난다면 루프를 빠져나옵니다
17. 포스트간 격자를 출력합니다
<br><br>

&nbsp; 블로그 포스트를 보여주기 위해 몇 가지 스타일을 추가했기 때문에 다음은 정의한 스타일을 사용할 수 있게 [``/assets/css/main.scss``](https://github.com/tareqdandachi/jekyll-shell-theme/blob/master/assets/css/main.scss) 를 수정합니다. 페이지 설계와는 관련 없지만 ``pre.highlight { white-space: pre-wrap; }`` 은 코드블록 안에서 자동 줄바꿈을 적용합니다.

```scss
...
.menu ul li.page_title { text-align: left; margin-left: 10px; float: left; font-weight: bold; color: var(--main-color) }

/* CUSTOMIZE */
.post-viewer { display: grid; width: 95%; height: 140px; grid-template-columns: 3fr 1fr; grid-gap: 10px; margin-top: 3%; margin-right: 2%; margin-bottom: 3%; margin-left: 2%; } /* 1 */
.post-content { grid-column: 1; } /* 2 */
.post-thumbnail { grid-column: 2; } /* 3 */
.thumbnail { width:100%; height:100%; object-fit: cover; } /* 4 */
.post-desc { overflow: hidden; text-overflow: ellipsis; white-space: nowrap; width: 400px; height: 25px; } /* 5 */
pre.highlight { white-space: pre-wrap; } /* 6 */

/* ERROR PAGES */
...
```
1. 포스트를 담을 격자 입니다
2. 포스트의 내용을 담을 틀에 해당합니다
3. 포스트의 썸네일을 담을 틀에 해당합니다
4. 썸네일의 형태를 정의합니다
5. ``description`` 텍스트가 400px를 넘어가면 뒷 내용을 ``...`` 으로 생략합니다
6. 코드블록 안에서 자동 줄바꿈을 적용합니다
<br><br>

&nbsp; 다음은 포스트를 만들기에 앞서 사실상 블로그의 핵심인 포스트의 레이아웃을 수정하겠습니다. [``/_layouts/post,html``](https://github.com/tareqdandachi/jekyll-shell-theme/blob/master/_layouts/post.html) 을 다음과 같이 수정하면 됩니다. 마찬가지로 주석을 달아 내용을 정리했습니다.

```html
{% raw %}---
layout: default
---

{%- if page.detail_image -%}
  <img class="detail_header" src="{{ page.detail_image }}">

{%- endif -%}

<div style="text-align: left;">
  <h1>{{ page.post-title }}</h1> <!-- 1 -->
</div>
<br>

<div>
  description: {{ page.description }} <!-- 2 -->
</div>
<br>

<div style="text-align: left;">
  {% assign date_split = page.date | split: " " %} <!-- 3 -->
  <i>
	created: {{ date_split[0] }} <!-- 4 -->
	<br>

	last_modified_at: {{ page.last_modified_at | date: '%Y-%m-%d' }} <!-- 5 -->
  </i>
</div>
<div style="text-align: left;">
  <span>
    tags:

    {% for tag in page.tags %}
      <a href="/tags/{{ tag }}">
		<code>
		  <nobr>{{ tag }}</nobr> <!-- 6 -->
	    </code>
	  </a>
	  &nbsp;

    {% endfor %}

  </span>
</div>
<br>

{{ content }}{% endraw %} <!-- 7 -->
```
1. 포스트의 타이틀을 출력합니다
2. 포스트에 대한 간단한 설명을 출력합니다
3. 포스트 페이지의 date 태그를 날짜만 출력하기 위해 ``" "`` 단위로 쪼개어 만들어진 리스트를 ``date_split``에 할당합니다
4. 포스트 생성 날짜를 출력합니다
5. 처음에 [``/Gemfile``](https://github.com/tareqdandachi/jekyll-shell-theme/blob/master/Gemfile) 에 정의하고 설치한 gem으로 포스트가 마지막으로 생성된 날짜를 출력합니다
6. 링크가 걸린 태그들을 하나 하나씩 출력합니다
7. 포스트의 콘텐츠를 출력합니다
<br><br>

&nbsp; 다음은 태그 클라우드 페이지와 각 테그들의 페이지를 추가합니다. 페이지 추가 이전에 ``/_includes`` 에 태그 클라우드에 대해 정의하여 필요할때마다 쉽게 불러올 수 있게 하겠습니다. 우선 포스트가 이미 존재한다는 가정하에 다음 작업을 진행하겠습니다. 우선 모든 포스트들의 ``front matter`` 에서 ``tags`` 에 정의된 태그들을 전부 모아야 합니다. 따라서 ``/_includes/tag_collect.html`` 을 생성하고 아래와 같이 수정합니다. 계속해서 주석을 이용한 설명은 언급없이 달도록 하겠습니다.

```html
{% raw %}{% assign rawtags = "" %}

{% for post in site.posts %}
  {% assign ttags = post.tags | join:'|' | append:'|' %}
  {% assign rawtags = rawtags | append:ttags %} <!-- 1 -->

{% endfor %}

{% assign site.tags = "" %}

{% for tag in rawtags %}

  {% if tag != "" %}

	{% if tags == "" %}
	  {% assign tags = tag | split:'|' %} <!-- 2 -->

	{% endif %}

	{% unless tags contains tag %}
	  {% assign tags = tags | join:'|' | append:'|' | append:tag | split:'|' %} <!-- 3 -->

	{% endunless %}

  {% endif %}

{% endfor %}{% endraw %}
```
1. ``ttags`` 를 할당하여 모든 포스트의 태그들을 ``|`` 단위로 나누고 포스트에서 만들어진 태그 묶음을 ``rawtags`` 에 추가합니다
2. ``rawtags`` 에 있는 태그묶음 들이 ``|`` 단위로 나뉘어져 있기 때문에 ``|`` 단위로 쪼개어 ``tags`` 에 할당합니다
3. ``tag`` 가 ``tags`` 에 포함되어 있지 않으면 포함시킵니다
<br><br>

&nbsp; 이렇게 만들어진 ``tags`` 라는 변수는 모든 페이지에서 항상 존재해야 사용이 간편합니다. 따라서 [``/_includes/head.html``](https://github.com/tareqdandachi/jekyll-shell-theme/blob/master/_includes/head.html)에 방금 생성한 소스 ``_includes/tag_collect.html`` 를 include 합니다. 이렇게 해서 ``site.tags`` 에 생성된 태그들이 모이게 됩니다.

```html
...
{% raw %}</title>

{% if site.tags != "" %}
  {% include tag_collect.html %}

{% endif %}

<link rel="stylesheet" href="{{ '/assets/css/main.css' | relative_url }}">{% endraw %}
...
```
<br>

&nbsp; 다음은 태그들을 모아두었기 때문에 태그 페이지를 만들기에 앞서 해당 태그의 포스트에 쉽게 접근할 수 있게 **태그 클라우드** 기능을 만듭니다. ``/_includes/tag_cloud.html`` 을 생성하고 아래와 같이 수정합니다.

```html
{% raw %}<div>
  <h1>Tags</h1> <!-- 1 -->
  <hr>

  {% capture temptags %}

    {% for tag in site.tags %}
      {{ tag[0] }} <!-- 2 -->

    {% endfor %}

  {% endcapture %}

  {% assign sortedtemptags = temptags | split:' ' | sort %} <!-- 3 -->

  {% for temptag in sortedtemptags %}
    <a href="/tags/{{ temptag }}">
	  <nobr>{{ temptag }}</nobr> <!-- 4 -->
    </a>
    &nbsp;

  {% endfor %}

  <hr>
</div>{% endraw %}
```
1. ``Tags`` 를 출력합니다
2. 사이트에 있는 태그들을 전부 ``temptags`` 에 추가합니다
3. 모인 태그를 쪼개고 정렬하여 ``sortedtemptags`` 에 할당합니다
4. 링크가 달린 태그를 하나 하나씩 출력합니다
<br><br>

&nbsp; 만들어진 태크 클라우드를 사용해서 태그 페이지를 만들도록 하겠습니다. 테그 페이지를 만들기 위해서는 따로 태그 페이지의 레이아웃을 정의해야 합니다. 따라서 저는 ``/_layouts/tags.html`` 을 생성하고 다음과 같이 수정했습니다.

```html
{% raw %}---
layout: default
---

<img class="home_header" src="/assets/images/main/site_main_title_green.png">
{% include tag_cloud.html %}{% endraw %}
```
<br><br>

&nbsp; 태그 페이지는 접근이 용이해야 좋으니 ``/tags.md``를 생성하고 메뉴바에 추가하기 위해 ``/_config.yml`` 의 ``header_pages`` 에 페이지를 등록합니다. 또한 ``/blog.md``에 대한 페이지도 이미 생성이 되었으니 마찬가지로 등록합니다.

```markdown
---
layout: tags
permalink: /tags
permalink_name: /tags
title: tags
---
```
<br>

```yml
# _config.yml
...
header_pages:
  - index.md
  - blog.md
  - tags.md
  - about.md
...
```
<br>

&nbsp; 메뉴바에 해당하는 페이지의 생성은 끝났지만 아직 각각의 태그들에 대한 페이지를 생성하지는 않았습니다. 따라서 포스트들에 있는 태그를 모아서 자동으로 태그 페이지를 생성하는 소스 ``/tag_generator.py`` 를 만듭니다. 소스는 ``python3`` 로 작성되었습니다. 이 스크립트는 포스트의 태그를 수정할 때 마다 한번씩 실행해야합니다.

```python
#!/usr/bin/env python
# tag_generator.py

import glob
import os
from ast import literal_eval

post_dir = '_posts/'
tag_dir = 'tags/'
filenames = glob.glob(post_dir + '*md')

if not os.path.exists(tag_dir):
    os.makedirs(tag_dir) # 1

total_tags = []

for filename in filenames:
	f = open(filename, 'rt', encoding='utf-8')
	flag = False # 2

	for l in f:

		if (flag):
			c_matter = l.strip().split(':')

			if (c_matter[0] == 'tags'):

				if (c_matter[1].strip().startswith('[')):
					clean_tags = ''.join(c for c in c_matter[1] if c not in '[]')
					list_tags = map(str.strip, clean_tags.split(','))
					total_tags.extend(list_tags) # 3

				else:
					list_tags = map(str.strip, c_matter[1].strip().split())
					total_tags.extend(list_tags) # 4

				flag = False

				break

		if (l.strip() == "---"):

			if (flag):
				flag = False

				break

			else:
				flag = True

	f.close()

total_tags = set(total_tags) # 5
pre_tags = glob.glob(tag_dir + "*.md")

for tag in pre_tags:
	os.remove(tag) # 6

for tag in total_tags:
	tag_filename = tag_dir + tag.replace(' ', '_') + '.md'
	f = open(tag_filename, 'at') # 7
	write_str = f'---\nlayout: tag\ntitle: \"Selected: {tag}\"\npermalink: tags/{tag}\npermalink_name: tags/{tag}\n\ntags: {tag}\n---\n'
	f.write(write_str)
	f.close()

print("Tags generated, count", total_tags.__len__()) # 8
```
1. ``/tags`` 디렉토리가 없다면 생성합니다
2. 포스트에서 ``front matter`` 에 해당되는 ``line`` 을 읽는 중이면 ``True`` 아니면 ``False`` 가 됩니다
3. 현재 포스트의 ``front matter`` 에 ``tags`` 가 리스트 형태로 정의되어 있다면 그 태그들을 모두 ``total_tags``에 추가합니다
4. 현재 포스트의 ``front matter`` 에 ``tags`` 가 하나의 문자열로 되어 있다면 태그를 ``total_tags`` 에 추가합니다
5. ``total_tags`` 는 모든 포스트들을 순회하며 태그들을 모았기 때문에 중복되는 태그가 있을 것입니다. ``set`` 타입 으로 변환하면 중복을 제거하며 동시에 자동으로 태그들을 사전순으로 정렬이 가능합니다.
6. 기존에 생성된 태그 페이지들을 모두 제거합니다.
7. ``total_tags`` 의 모든 태그 페이지들을 생성합니다
8. 만들어진 태그 페이지의 수를 출력합니다
<br><br>

&nbsp; 모든 태그에 대한 태그 페이지가 만들었습니다. 하지만 ``/tag_generator.py`` 에서 ``layout`` 으로 정의한 파일이 없기 때문에 아직은 개별적인 태그에 대한 포스트를 볼 수는 없습니다. 따라서 ``/_layouts/tag.html`` 를 생성합니다. ``/_layouts/tag.html`` 은 ``/_layouts/blog.html`` 와 중복되는 부분이 많기 때문에 중복되는 부분은 아래의 설명에서 생략하겠습니다.

```html
{% raw %}---
layout: default
---

<img class="home_header" src="/assets/images/main/site_main_title_green.png">
{% include tag_cloud.html %}
<br>

<h3>{{ page.title }}</h3>
<hr>
<ul>{% assign lastpost = site.tags[page.tags] | last %} <!-- 1 -->
  {% for post in site.tags[page.tags] %} <!-- 2 -->
	...

	<hr>

  {% endfor %}

</ul>{% endraw %}
```
1. 해당 페이지에 front matter 의 tags 에 정의된 태그를 가진 포스트들을 가져오고 격자 생성을 멈춰줄 마지막 포스트를 할당합니다
2. blog.html과 중복되는 부분입니다
<br><br>

&nbsp; 마침내 모든 초기화 과정이 끝났습니다. 이제 포스트를 하나 생성해봅니다. 포스트를 생성할 때 주의할 점은 포스트는 항상 ``/_post`` 에 있어야 한다는 점, 포스트의 파일명이 항상 ``2022-06-28-title.md`` 형식이어야 한다는 점, 제가 위에서 설명한 소스들을 사용하기 위해서 모든 포스트들의 front matter의 형식을 아래의 코드블록의 형식으로 작성해야 된다는 점입니다. ``date`` 는 파일의 생성 날짜인데 약간은 불편하지만 파일을 생성할 때의 파일명을 가져와 붙여넣습니다. 시간은 현재 시간을 적으면 됩니다.

```markdown
---
layout: post
title: 제목
post-title: 제목
date: 2022-06-28-12 08:34:00 +0900
permalink: /blog/title.html
permalink_name: /blog/title
category: blog
description: 사이트 테스트를 위한 포스트입니다.
tags: [메모장, test]

detail_image: /assets/images/thumb/first_post.jpg
---
...
```
<br>

&nbsp; 이제 포스트가 하나 만들어져 있기 때문에 ``/tag_generator.py`` 를 실행하면 태그 페이지가 생성될 것입니다. 터미널에서 파이썬 스크립트를 실행하면 되겠습니다.

```shell
python3 tag_generator.py
```
<br>

&nbsp; 마지막으로 /_config.yml 의 수정사항을 다시 블로그에 적용하기 위해 터미널에 ``bundle install --redownload`` 를 실행합니다.

```shell
bundle install --redownload
```
<br>

&nbsp; 지금까지의 과정이 모두 막힘없이 진행되었다면 저와 같은 형태의 블로그를 운영할 수 있을 것입니다. 제가 수정한 템플릿이 마음에 든다면 그대로 적용하여 사용해도 좋지만 아래와 같이 출처를 남겨주셔야 합니다.
<br>

# 마치며
&nbsp; 저는 이 블로그를 만들기 이전에 이미 한번 블로그를 만들어본 경험이 있었습니다. 하지만 그 당시에는 저도 처음 접하는 언어의 문법에 의해 어떤 오픈소스도 손대보지 못하고 정해진 형식대로 마음에 들지않는 블로그를 사용하다 결국 그만두었습니다. 하지만 이번에 이전에 생성한 사이트를 미련없이 밀어버리고 새로 블로그를 시작하면서 확실히 소스를 읽고 구현하는 능력이 많이 향상되었음을 느낍니다. 이번에는 마음에 드는 형태로 ~~온전하게 사이트가 구현이 되었기 때문에~~ (수정일자에 문제가 생겼습니다) 굉장히 성취감이 큽니다. 앞으로도 수정사항이 있다면 계속해서 게시물을 업데이트 하겠습니다. 이것으로 포스트를 마칩니다. 감사합니다.
<br>

---

# Reference URL
- [https://github.com/tareqdandachi/jekyll-shell-theme/](https://github.com/tareqdandachi/jekyll-shell-theme/ "jekyll theme i set")
- [https://github.com/uml-embedded/uml-embedded.github.io/](https://github.com/uml-embedded/uml-embedded.github.io/ "source i referenced")
- [https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Grid_Layout](https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Grid_Layout "grid layout")
- [https://longqian.me/2017/02/09/github-jekyll-tag/](https://longqian.me/2017/02/09/github-jekyll-tag/ "how to create tag pages")
- [https://syki66.github.io/blog/2020/02/08/clean-blog-highlighter.html](https://syki66.github.io/blog/2020/02/08/clean-blog-highlighter.html "code block auto line break")
- [https://stackoverflow.com/questions/45290135/](https://stackoverflow.com/questions/45290135/how-do-i-force-bundler-to-reinstall-all-of-my-gems "how do i force bundler to reinstall all of my gems")

---
layout: post
title: 마지막 수정일자 표기
post-title: 마지막 수정일자 표기
date: 2022-07-21 11:03:00 +0900
# last_modified_at:
permalink: /blog/jekyll_themes.html
permalink_name: /blog/jekyll_themes
category: blog
description: 블로그 생성 도중 발생한 이슈였던 마지막 수정일자 자동표기 방법에 대해 명시합니다.
tags: [liquid, html, jekyll, java_script]

detail_image: /assets/images/thumb/octocat_jekyll.jpg
---

&nbsp; 본 게시물에서는 이전 포스트에서 발생한 이슈인 마지막 수정일이 자동으로 표기되지 않았던 문제에 대해 다룹니다.

---
&nbsp; 블로그를 호스팅하게 되면서 여러가지 편리한 기능들을 만들어 활용하려 했지만 기능을 만드는데 문제점이 발생하고 있습니다. 저같은 경우에는 [``jekyll-last-modified-at``](https://github.com/gjtorikian/jekyll-last-modified-at) 이라는 플러그인을 사용해 마지막 수정일자를 자동으로 표기할 수 있는 변수를 만들어 활용하고자 했지만 플러그인 자체가 [``깃허브 페이지의 화이트리스트``](https://github.com/github/pages-gem/blob/master/lib/github-pages/plugins.rb)에 등록되지 않아 로컬에서는 사용이 가능하지만 호스팅 할 때는 불가능합니다. 하지만 자바스크립트를 활용하여 [``이 기능을 구현하는 포스트``](https://ryanfb.github.io/etc/2020/04/27/last_modified_dates_for_github_pages_jekyll_posts.html)를 발견하여 잠시 소개하기 위해 이 글을 작성하게 되었습니다.

&nbsp; 마지막 표기일을 자동으로 생성하는 방법으로 대부분의 레퍼런스들이 커밋 로그를 이용합니다. 위에 언급된 플러그인 (jekyll-last-modified-at) 조차도 커밋 로그를 활용해 자동 수정일자를 만듭니다. 자바스크립트를 배우진 않았지만 이 방법 또한 마찬가지로 커밋 로그를 활용하는 것 처럼 보입니다. 기능을 구현하기 위해서 우선은 jekyll-github-metadata 라는 플러그인이 필요합니다.

```shell
# Gemfile
...

group :jekyll_plugins do
  gem 'jemoji'
  # gem 'jekyll-last-modified-at'
  gem 'jekyll-github-metadata' # 추가
end
```
<br>

```yml
# _config.yml
...
plugins:
  - jemoji
  - jekyll-sitemap
  - jekyll-seo-tag
  - jekyll-github-metadata # 추가
...
```
<br>

&nbsp; 플러그인 사용을 위해 일단은 위와같이 파일을 변경합니다. 위의 변경사항을 사이트에 적용하려면 아마도 ``bundle install``을 한번 실행해야 할 것입니다. 그리고 마지막 수정일자 표기를 위해 아래 함수를 ``_include/head.html``에 작성합니다.

```html
{% raw %}<!-- _include/head.html -->

...
<script type="text/javascript">
  function setModifiedDate() {

    if (document.getElementById('last-modified')) {
      fetch("https://api.github.com/repos/{{ site.github.owner_name }}/{{ site.github.repository_name }}/commits?path={{ page.path }}")
        .then((response) => {

          return response.json();
        })

        .then((commits) => {
          var modified = commits[0]['commit']['committer']['date'].slice(0,10);
          if(modified != "{{ page.date | date: "%Y-%m-%d" }}") {
            document.getElementById('last-modified').textContent = "Last Modified: " + modified;
          }

        });

    }

  }
</script>
...{% endraw %}
```
<br>

&nbsp; ``_include/head.html`` 에 작성된 함수를 블로그 포스트에 적용하기 위해서 ``_layouts/default.html`` 의 body 태그의 onload 이벤트로 작성한 함수를 줍니다.

```html
{% raw %}<!-- _layouts/default.html -->

...
  <body class="{{ site.font-size }}" onload="setModifiedDate();">
    {% include header.html %}
    {{ content }}
    {% include footer.html %}
  </body>
...{% endraw %}
```
<br>

&nbsp; 마지막으로 ``_layout/post.html``에서 span 태그를 사용해 이전 코드를 수정합니다.

```html
<!-- _layout/post.html -->

...
<div style="text-align: left;">
  {% assign date_split = page.date | split: " " %}
  <i>
    <span>created: {{ date_split[0] }}</span>
    <br>

    <!-- last_modified_at: {{ page.last_modified_at | date: '%Y-%m-%d' }} -->
    <span id='last-modified'/>
  </i>
</div>
...
```
<br>

&nbsp; 이제 변경사항을 commit 하고 원격 저장소로 push 하게되면 간단하게 마지막 수정일자를 표시할 수 있습니다.
<br>

---

# Reference URL
- [https://ryanfb.github.io/](https://ryanfb.github.io/etc/2020/04/27/last_modified_dates_for_github_pages_jekyll_posts.html)

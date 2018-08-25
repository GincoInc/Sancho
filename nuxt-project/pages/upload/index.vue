<template>
<div>

<!-- header -->
<header>
  <div class="wrapper_contents_header">
    <h1 class="logo_header">
      <a href="/">
        <img src="~/assets/logo_header.png" title="SANCHO" alt="SANCHOロゴ">
      </a>
    </h1>
    <div class="wrapper_form_header">
      <div class="wrapper_balance_header">
        <span class="subtitle_balance_header">アドレス:</span>
        <span class="balance_header">AMdDsjNcxirRnYST4iLPFDJB5E6woYPdjK</span>
      </div>
      <button class="button_go_header">Upload</button>
    </div>
  </div>
</header>

<!-- detail -->
<section id="detail">
  <div class="wrapper_contents_detail">
    <div class="info_detail">
      <h2 class="title_book_detail">マンガをアップロードする</h2>
      <p class="description_book_detail">こちらからマンガのアップロードをおこなってください</p>
      <div class="wrapper_form_header">
      <a class="button_upload_header">アップロード開始</a>
    </div>
    </div>
  </div>
</section>

<!-- archives -->
<section id="archives">
  <ul class="wrapper_contents_archives">
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_01.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_02.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_03.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_04.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_05.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_06.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_01.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_02.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_03.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_04.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_05.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_06.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_01.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
    <li class="each_book_archives">
      <article class="thumbnail_archives">
        <a href="#">
          <img src="~/assets/thumbnail_book_02.jpg" title="manga name" alt="サムネイル画像">
        </a>
      </article>
    </li>
  </ul>
</section>

<!-- footer -->
<footer>
  <div class="wrapper_contents_footer">
    <span class="copyright">©2018 SANCHO All Rights Reserved.</span>
    <h2 class="logo_footer">
      <a href="//ginco.io" target="_blank">
        <img src="~/assets/logo_header.png" title="Ginco" alt="ロゴ画像">
      </a>
    </h2>
    <div class="wrapper_right_footer">
      <ul class="sns_footer">
        <li class="each_sns">
          <a href="">
            <i class="fab fa-twitter"></i>
          </a>
        </li>
        <li class="each_sns">
          <a href="">
            <i class="fab fa-facebook-f"></i>
          </a>
        </li>
      </ul>
    </div>
  </div>
</footer>

</div>
</template>


<script>
</script>


<style>
@charset "UTF-8";

/* header */
header {
  z-index: 9999;
  position: fixed;
  width: 100%;
  background: #000;
	box-shadow: 0px 5px 20px rgba(0, 0, 0, .3);
}
header .logo_header {
  width: 120px;
}
header .logo_header a {
  display: -webkit-flex;
  -webkit-flex-direction: column;
  -webkit-justify-content: center;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
header .logo_header img {
  width: 100%;
  height: auto;
}
header .wrapper_contents_header {
  width: 1300px;
  display: -webkit-flex;
  -webkit-align-items: center;
  -webkit-justify-content: space-between;
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 0px auto;
  padding: 10px 0;
}
header .rapper_form_header {
  display: -webkit-flex;
  -webkit-align-items: center;
  display: flex;
  align-items: center;
}
header .button_go_header {
  background: #fff100;
  height: 40px;
  font-family: 'Oswald', sans-serif;
  -webkit-appearance: none;
  appearance: none;
  border-radius: 20px;
  width: 120px;
  text-align: center;
  font-size: 14px;
  font-weight: bold;
  border: none;
  margin-left: 10px;
}
header .wrapper_balance_header {
  width: auto;
  border-bottom: solid 2px #fff;
  display: -webkit-flex;
  -webkti-align-items: center;
  display: flex;
  align-items: center;
  margin-right: 20px;
  padding-bottom: 2px;
  margin-left: auto;
}
header .wrapper_form_header {
  display: -webkit-flex;
  -webkit-align-items: center;
  display: flex;
  align-items: center;
  width: 600px;
  margin-left: auto;
}
header .subtitle_balance_header {
  color: #fff;
  font-size: 15px;
  margin-right: 10px;
}
header .balance_header {
  color: #fff;
  font-size: 14px;
  font-weight: bold;
}

/* detail */
#detail {
  width: 100%;
  height: 500px;
  padding-top: 60px;
  display: -webkit-flex;
  -webkit-flex-direction: column;
  -webkit-justify-content: center;
  flex-direction: column;
  display: flex;
  justify-content: center;
}
#detail .wrapper_contents_detail {
  display: -webkit-flex;
  display: flex;
  margin: 0 auto;
  width: 800px;
}
#detail .info_detail {
  width: 100%;
  display: -webkit-flex;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
#detail .title_book_detail {
  font-size: 40px;
  text-align: center;
}
#detail .description_book_detail {
  font-size: 14px;
  color: #777;
  text-align: center;
  margin-top: 10px;
}
#detail .button_upload_header {
  background: #1e5ccc;
  display: block;
  padding: 20px 0;
  font-family: 'Oswald', sans-serif;
  -webkit-appearance: none;
  appearance: none;
  border-radius:1200px;
  color: #fff;
  font-size: 14px;
  width: 100%;
  text-align: center;
  font-weight: bold;
  border: none;
  box-shadow: 0px 15px 30px rgba(0, 0, 0, .1);
}
#detail .wrapper_form_header {
  margin-top: 40px;
}

/* archives */
#archives {
  padding: 0px 0 160px;
}
#archives .wrapper_contents_archives {
  letter-spacing: -.4em;
  width: 1000px;
  margin: 0 auto;
}
#archives .each_book_archives {
  width: 16.8%;
  margin-right: 4%;
  overflow: hidden;
  margin-bottom: 40px;
  border-radius: 4px;
  letter-spacing: normal;
  display: inline-block;
  vertical-align: top;
}
#archives .each_book_archives:nth-of-type(5n) {
  margin-right: 0%;
}
#archives .thumbnail_archives {
  box-shadow: 0px 15px 30px rgba(0, 0, 0, .2);
  width: 100%;
  height: 180px;
  background-color: #f5f5f5;
}
#archives .thumbnail_archives > a {
  display: block;
  width: 100%;
  height: 100%;
}

/* footer */
footer {
  background: #000;
  padding: 60px 0 60px;
}
footer .logo_footer {
  width: 85px;
}
footer .logo_footer a {
  display: block;
}
footer .logo_footer img {
  width: 100%;
  height: auto;
}
footer .wrapper_contents_footer {
  position: relative;
  width: 980px;
  margin: 0 auto;
  display: -webkit-flex;
  -webkit-align-items: center;
  -webkit-justify-content: space-between;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
footer .wrapper_right_footer {
  display: -webkit-flex;
  -webkit-align-items: center;
  display: flex;
  align-items: center;
}
footer .contact_footer {
  font-size: 12px;
  text-decoration: underline;
  margin-right: 30px;
  color: #ccc;
}
footer .copyright {
  font-size: 10px;
  position: absolute;
  width: 190px;
  right: 0;
  left: 0;
  margin: auto;
  text-align: center;
  color: #555;
}
footer .sns_footer {
  display: -webkit-flex;
  -webkit-align-items: center;
  display: flex;
  align-items: center;
}
footer .each_sns {
    margin-right: 30px;
}
footer .each_sns:last-child {
    margin-right: 0px;
}
footer .each_sns > a {
    display: block;
}
footer .each_sns > a:hover .fa-twitter {
    color: #55acee;
}
footer .each_sns > a:hover .fa-facebook-f {
    color: #3B5998;
}
footer .fa-twitter {
    font-size: 21px;
    color: #ccc;
}
footer .fa-facebook-f {
    font-size: 19px;
    color: #ccc;
}
</style>


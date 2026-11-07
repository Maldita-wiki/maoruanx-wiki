---
sidebar_position: 1
title: éè¦å¯ç¨ JavaScript
slug: /game/fivem/absolute/use
---

<article><div class="theme-doc-markdown markdown"><header><h1>Absolute ä½¿ç¨æç¨</h1></header>
<p><strong><span class="text-grey">Absolute èåæ³¨åãä¸è½½åä½¿ç¨è¯¦ç»æç¨</span></strong></p>
<div class="theme-admonition theme-admonition-danger admonition_LJt0 alert alert--danger"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 12 16"><path d="M5.05.31c.81 2.17.41 3.38-.52 4.31C3.55 5.67 1.98 6.45.9 7.98c-1.45 2.05-1.7 6.53 3.53 7.7-2.2-1.16-2.67-4.52-.3-6.61-.61 2.03.53 3.33 1.94 2.86 1.39-.47 2.3.53 2.27 1.67-.02.78-.31 1.44-1.13 1.81 3.42-.59 4.78-3.42 4.78-5.56 0-2.84-2.53-3.22-1.25-5.61-1.52.13-2.03 1.13-1.89 2.75.09 1.08-1.02 1.8-1.86 1.33-.67-.41-.66-1.19-.06-1.78C8.18 5.31 8.68 2.45 5.05.32L5.03.3l.02.01z" fill-rule="evenodd"></path></svg></span>æ¨éè¦æ¥æRedENGINEæ¬ä½æå¯è´­ä¹°è¯¥Luaäº§å</div></div>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="preface"><strong>åè¨</strong><a aria-label="prefaceçç´æ¥é¾æ¥" class="hash-link" href="#preface" title="prefaceçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="theme-admonition theme-admonition-tip admonition_LJt0 alert alert--success"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 12 16"><path d="M6.5 0C3.48 0 1 2.19 1 5c0 .92.55 2.25 1 3 1.34 2.25 1.78 2.78 2 4v1h5v-1c.22-1.22.66-1.75 2-4 .45-.75 1-2.08 1-3 0-2.81-2.48-5-5.5-5zm3.64 7.48c-.25.44-.47.8-.67 1.11-.86 1.41-1.25 2.06-1.45 3.23-.02.05-.02.11-.02.17H5c0-.06 0-.13-.02-.17-.2-1.17-.59-1.83-1.45-3.23-.2-.31-.42-.67-.67-1.11C2.44 6.78 2 5.65 2 5c0-2.2 2.02-4 4.5-4 1.22 0 2.36.42 3.22 1.19C10.55 2.94 11 3.94 11 5c0 .66-.44 1.78-.86 2.48zM4 14h5c-.23 1.14-1.3 2-2.5 2s-2.27-.86-2.5-2z" fill-rule="evenodd"></path></svg></span>æ¸©é¦¨æç¤º</div><div class="admonitionContent__XZN"><ul>
<li class=""><strong>ä¿å­å¥½èªå·±çæ¿æ´»ç è·æ³¨åçè´¦å·å¯ç , è¥ä¸¢å¤±æ æ³æ¾ååæèªè´</strong></li>
<li class=""><strong>æ¬æç¨ä»åæ­£å¸¸æ­¥éª¤æ¼ç¤º, æ ¹æ®æç¨æä½åºç°é®é¢ä¼åèç³»ä½ çåå®¶è§£å³</strong></li>
<li class=""><strong>è¯·ä»ç»éè¯»ææåå®¹ä¸æç¤º,éå°é®é¢å°è¯åèªå·±è§£å³ (å¦åå© AI å·¥å·)</strong></li>
<li class=""><strong>æç¨å¯è½å·ææ¶ææ§,è¥ä¸éç¨è¯·åæ¶èç³»æ</strong></li>
</ul></div></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="status"><strong>èåç¶æ</strong><a aria-label="statusçç´æ¥é¾æ¥" class="hash-link" href="#status" title="statusçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="custom-link-card-container"><ul>
<li class=""><a class="" href="https://guide.maoruanx.com/home/state" rel="noopener noreferrer" target="_blank">ðèåç¶æ</a></li>
</ul></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="condition"><strong>å¿å¤ç¯å¢</strong><a aria-label="conditionçç´æ¥é¾æ¥" class="hash-link" href="#condition" title="conditionçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="environment-unified"><div class="environment-unified__heading">ä½¿ç¨åæ£æ¥</div><ol>
<li class=""><a class="" href="https://guide.maoruanx.com/misc/win/systemprotection" rel="noopener noreferrer" target="_blank"><strong>å³é­ææææ¯è½¯ä»¶</strong></a> <strong>(å¦ç¡®è®¤å·²å³å¹²åè¯·æ è§) /</strong> <strong><span class="text-blue"><code>å³é­CE ç­è°è¯è½¯ä»¶</code></span></strong></li>
<li class=""><strong><span class="text-blue"><code>å¸è½½è¾è®¯ACEåä½å¼</code></span></strong> <strong>(å¡å¿å¸è½½,å¸è½½åééå¯çµè,å¦ææ¨ä¸ç©è¾è®¯æ¸¸ææçµèä¸­æ²¡æACEåä½å¼åæ è§æ­¤æ¡),</strong> <a class="" href="https://guide.maoruanx.com/misc/win/ace" rel="noopener noreferrer" target="_blank"><strong>ç¹å»æ¥çå¸è½½è¾è®¯ACEåä½å¼æç¨</strong></a></li>
<li class=""><a class="" href="https://guide.maoruanx.com/misc/win/kernel" rel="noopener noreferrer" target="_blank"><strong>å³é­Windowsåæ ¸éç¦»</strong></a></li>
<li class=""><strong>å®è£</strong> <a class="" href="https://shark.lanzn.com/b0izso9af" rel="noopener noreferrer" target="_blank"><strong>è¿è¡åºåé</strong></a> <strong>(ä¸è½½ - è¿è¡ - ä¸è·¯ç»§ç»­ - èå¿ç­å¾å åéå³å¯,è¥æ¾å®è£è¿è¯·æ è§)</strong></li>
<li class=""><strong>è¿è¡ä¸æ¬¡</strong> <a class="" href="https://guide.maoruanx.com/misc/win/protection" rel="noopener noreferrer" target="_blank"><strong>æäººèæ¬</strong></a> <strong>(è¥æ¾è¿è¡è¿è¯·æ è§)</strong></li>
</ol><div class="environment-unified__foot">è¯·ä»¥æ¬é¡µè¦æ±ä¸ºåï¼ä¸åèåçå¿å¤ç¯å¢å¯è½ä¸åã</div></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="register"><strong>æ³¨å</strong><a aria-label="registerçç´æ¥é¾æ¥" class="hash-link" href="#register" title="registerçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="theme-admonition theme-admonition-danger admonition_LJt0 alert alert--danger"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 12 16"><path d="M5.05.31c.81 2.17.41 3.38-.52 4.31C3.55 5.67 1.98 6.45.9 7.98c-1.45 2.05-1.7 6.53 3.53 7.7-2.2-1.16-2.67-4.52-.3-6.61-.61 2.03.53 3.33 1.94 2.86 1.39-.47 2.3.53 2.27 1.67-.02.78-.31 1.44-1.13 1.81 3.42-.59 4.78-3.42 4.78-5.56 0-2.84-2.53-3.22-1.25-5.61-1.52.13-2.03 1.13-1.89 2.75.09 1.08-1.02 1.8-1.86 1.33-.67-.41-.66-1.19-.06-1.78C8.18 5.31 8.68 2.45 5.05.32L5.03.3l.02.01z" fill-rule="evenodd"></path></svg></span>éè¦æé</div><div class="admonitionContent__XZN"><ol>
<li class=""><strong>æ³¨åä»»ä½èåçè´¦å·å¯ç ä¸æ¸¸æåçå®å¨æ å³,ééåä½ çç¬ä¸æ äºçå¥½è®°ç,ä¸å»ºè®®è´¦å·å¯ç é½è¾å¥QQå·ç­å¾å®¹æè¢«ççä¿¡æ¯</strong></li>
<li class=""><strong>æ³¨åä»»ä½èåæå¥½åªä½¿ç¨</strong> <strong><code>æ°å­ + å­æ¯ç»å</code></strong> <strong>, é¿åº¦å¨ 8 ä½ä»¥ä¸,å°¤å¶ä¸è¦è¾å¥</strong> <strong><code>ä¸­æ</code></strong> <strong><code>ç©ºæ ¼</code></strong> <strong>ä¸</strong> <strong><code>ä¸­æç¬¦å·</code></strong> <strong>, ä¸æå°æ°èåä¸æ¯æ</strong> <strong><code>è±æç¬¦å·</code></strong></li>
<li class=""><strong>è¯·èªè¡ä¿ç®¡å¥½ææç¸å³ç æ¿æ´»ç /å¡å¯/è´¦å·ä¿¡æ¯,è¯·å¿æ³é²,é¨åèåæ²¡ææ¾åå¯ç æå¡,ä¸æ¬åºæ²¡ææä¾ç¸å³ä»£ç®¡ä¸å¡çä¹å¡ (æå­/åªæ¯ç»å¤§å®¶çç¦å©,è¯·ä¸è¦ä¾èµæ­¤æå¡),ä¸¢å¤±ç¸å³æ°æ®å¯¼è´çä»»ä½åæèªè¡æ¿æ</strong></li>
<li class=""><strong>æ³¨åæ¿æ´»å,ä½ è´¦æ·çè§£éæå½æ­¤è½¯ä»¶å¼åå¢éææ,ä¸ææ å³,è¯·ä¸¥æ ¼éµå®è§å (é¨åéè¦æå¸®å¿å¤ççæ¯å¦æ´æ¢æºå¨ç ,å±äºéå ç¦å©çä¸ç§,å æ¬åºå±äºä»£è´­æ§è´¨,è¯·å°½éèªå©å®æ),è¿åè½¯ä»¶è§åå¯¼è´çä»»ä½åæèªè¡æ¿æ (å¦ç»å¤§é¨åèåç¦æ­¢åäº«/äºæå¤çè´¦æ·)</strong></li>
</ol></div></div>
<p><strong>ç¹å»è·³è½¬æ³¨åé¡µé¢ï¼</strong></p>
<div class="custom-link-card-container"><p><a class="" href="https://redengine.eu/login" rel="noopener noreferrer" target="_blank">Register - RedENGINE</a></p></div>
<div style="text-align:center"><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tOzb5jZpQ4rtltdwh80.png"/><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tPZq1QuN41FtrQCv0iD.png"/></p></p></div>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="verify"><strong>éªè¯</strong><a aria-label="verifyçç´æ¥é¾æ¥" class="hash-link" href="#verify" title="verifyçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div style="text-align:center"><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tPCtCKJewn5v7w6Psrh.png"/><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tPYWYhPl21jBr0bWLHB.png"/></p></p></div>
<div class="theme-admonition theme-admonition-danger admonition_LJt0 alert alert--danger"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 12 16"><path d="M5.05.31c.81 2.17.41 3.38-.52 4.31C3.55 5.67 1.98 6.45.9 7.98c-1.45 2.05-1.7 6.53 3.53 7.7-2.2-1.16-2.67-4.52-.3-6.61-.61 2.03.53 3.33 1.94 2.86 1.39-.47 2.3.53 2.27 1.67-.02.78-.31 1.44-1.13 1.81 3.42-.59 4.78-3.42 4.78-5.56 0-2.84-2.53-3.22-1.25-5.61-1.52.13-2.03 1.13-1.89 2.75.09 1.08-1.02 1.8-1.86 1.33-.67-.41-.66-1.19-.06-1.78C8.18 5.31 8.68 2.45 5.05.32L5.03.3l.02.01z" fill-rule="evenodd"></path></svg></span>éè¦æé</div><div class="admonitionContent__XZN"><ul>
<li class=""><strong>è¯·</strong> <strong><code>ä¿ç®¡å¤ä»½å¥½</code></strong> <strong>èªå·±ç</strong> <strong><code>æ¿æ´»ç </code></strong> <strong>ä»¥å</strong> <strong><code>è´¦æ·ä¿¡æ¯</code></strong> <strong>,ä¸¢å¤±ä¹åæ æ³æ¾å!!æä»¬ä¸æä¾ä»»ä½å¸æ·ä¿ç®¡æå¡!</strong></li>
<li class=""><strong>åç»­ç½ç«ä¹ä¸ä¼å¸®å¤ä»½ä½ çæ¿æ´»ç ä¿¡æ¯,è¯·ä½ èªè¡</strong> <strong><code>ä¿å­</code></strong> <strong>!</strong></li>
<li class=""><strong>æ³¨åæ¿æ´»ä¹å,è¯¥è´¦æ·ä¸æä»¬åæ å³è,ææçè´¦æ·ä¿¡æ¯,åç±ä½ ä¸ªäººåç¬è¿è¡ç»´æ¤åä½¿ç¨,è¯·èªè§éµå®åä¸ªèåè§å!</strong></li>
</ul></div></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="subscription"><strong>æ¿æ´»</strong><a aria-label="subscriptionçç´æ¥é¾æ¥" class="hash-link" href="#subscription" title="subscriptionçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div style="text-align:center"><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tOvkPxlfnoRloTaPtDp.png"/></p></div>
<p><strong>æ¿æ´»æååå¦å¾æç¤º</strong></p>
<div style="text-align:center"><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tOwnuasW7IKlWNgIpmV.png"/></p></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="download"><strong>ä¸è½½</strong><a aria-label="downloadçç´æ¥é¾æ¥" class="hash-link" href="#download" title="downloadçç´æ¥é¾æ¥" translate="no">â</a></h2>
<div class="theme-admonition theme-admonition-info admonition_LJt0 alert alert--info"><div class="admonitionHeading_PJt7"><span class="admonitionIcon_dA2l"><svg viewbox="0 0 14 16"><path d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z" fill-rule="evenodd"></path></svg></span>å°è´´å£«</div><div class="admonitionContent__XZN"><p><strong>æ°¸è¿å»æä¸ä¸ªå¥½ä¹ æ¯:ä¸è½½ä»»ä½ç¨åºä¸è¦ä¸å°å« ä¸­æ/ä¸­æç¬¦å·/å¥æªå­ç¬¦ çæä»¶å¤¹ä¸­,è¿å¯è½å¯¼è´é¨åç¨åºè¿è¡ä¸äº;å¹¶å»ºè®®å°åä¸ªç¨åº/åç¼©åæ¾å¥åç¬çæä»¶å¤¹ä¸­,é²æ­¢é¨åç¨åºéæ¾åºå¾å¤é²ææä»¶æè§£ååºå¤ªå¤æä»¶å½±åæ´æ´åº¦</strong></p></div></div>
<div style="text-align:center"><p><img alt="" class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tPU0K8bqwxRveGTlS6O.png"/></p></div>
<h3 class="anchor anchorTargetStickyNavbar_lorJ" id="booster"><strong>å éå¨</strong><a aria-label="boosterçç´æ¥é¾æ¥" class="hash-link" href="#booster" title="boosterçç´æ¥é¾æ¥" translate="no">â</a></h3>
<blockquote>
<p><strong>ç½ç»ä¸å¥½çå¡å¿èªå·±ä½¿ç¨ç§å­¦ä¸ç½</strong><br/>
<strong>ç¦æ­¢ä½¿ç¨<span class="text-blue"><code>åè´¹å éå¨</code></span></strong><br/>
<strong><span class="text-blue"><code>é·ç¥/èè·/é²ç</code></span>ç­å éå¨è¿ææè°ç<span class="text-blue"><code>å éå¨çå­</code></span>èªè¡å°è¯,ä¸è¡å°±æ¢ä¸åå éå¨</strong></p>
<blockquote>
<ul>
<li class=""><strong><a class="" href="https://uu.163.com/" rel="noopener noreferrer" target="_blank">UU</a>ï¼è·¯ç±æ¨¡å¼/æ¨¡å¼ 3 (UU/å¥æ¸¸ç¸å¯¹æç¨³)</strong></li>
<li class=""><strong><a class="" href="https://www.qiyou.cn/" rel="noopener noreferrer" target="_blank">å¥æ¸¸</a>ï¼æ¨¡å¼ 1 (UU/å¥æ¸¸ç¸å¯¹æç¨³)</strong></li>
<li class=""><strong><a class="" href="https://www.xunyou.com/" rel="noopener noreferrer" target="_blank">è¿æ¸¸</a>ï¼æ¨¡å¼ 3 (èçä¹ä¸é)</strong></li>
<li class=""><strong><a class="" href="https://www.akspeedy.com/" rel="noopener noreferrer" target="_blank">AK</a>ï¼æ¨¡å¼ 5 (èªç¨æ¨è,æ§ä»·æ¯é«,æ¶é¿è®¡ç®,ä¸è¡ç¨ æ¨¡å¼ 4)</strong><br/>
<strong><span class="text-purple">å°è¯æ´æ¢å éå¨ æ´æ¢å éå¨æ¨¡å¼ æ´æ¢å éå¨èç¹ ç´å°è½æ³¨å¥ä½¿ç¨ä¸ºæ­¢</span></strong></li>
</ul>
</blockquote>
</blockquote>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="injection"><strong>æ³¨å¥</strong><a aria-label="injectionçç´æ¥é¾æ¥" class="hash-link" href="#injection" title="injectionçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p><strong>å¨æ³¨å¥çº¢æå¹¶ç¡®ä¿å¯ä»¥æ­£å¸¸ä½¿ç¨çæåµä¸,å¼å¯ä»¥ä¸åè½</strong></p>
<div style="text-align:center"><p><img alt=" " class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tPY3MIZxzrCP90PSmEP.png"/></p></div>
<div style="text-align:center"><p><img alt=" " class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tP71JEajqXaYhI2VyGr.png"/></p></div>
<p><strong>å å¥æå¡å¨å¹¶å¼åºçº¢æèå</strong></p>
<div style="text-align:center"><p><img alt=" " class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tPCAZ3jQBxLK1de5CAn.png"/></p></div>
<p><strong>ç¶åå è½½ä½ éè¦çèå,ç¹å»<code>Run Menu</code></strong></p>
<div style="text-align:center"><p><img alt=" " class="img_i2Xa" decoding="async" loading="lazy" src="https://pic1.imgdb.cn/i/034tPDhXjnHuYLcN1UauYB.png"/></p></div>
<hr/>
<h2 class="anchor anchorTargetStickyNavbar_lorJ" id="shortcut-key"><strong>ä½¿ç¨</strong><a aria-label="shortcut-keyçç´æ¥é¾æ¥" class="hash-link" href="#shortcut-key" title="shortcut-keyçç´æ¥é¾æ¥" translate="no">â</a></h2>
<p><strong>å è½½å¯¹åºçLuaèå,å¹¶è®¾ç½®å¼åºé®</strong></p>
<!-- -->
<div class="theme-tabs-container tabs-container tabList_TYeX"><ul aria-orientation="horizontal" class="tabs" role="tablist"><li aria-selected="true" class="tabs__item tabItem_v163 tabs__item--active" role="tab" tabindex="0">é¼ æ æä½</li></ul><div class="margin-top--md"><div class="tabItem_xKIf" role="tabpanel"><p><strong><code>F10</code> å¼åº/éèèå</strong><p><strong><code>é¼ æ å³é®</code>ç¹å» ææ§ç»å®èå</strong></p></p></div></div></div></div></article>
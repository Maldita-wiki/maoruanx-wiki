---
sidebar_position: 1
title: Reverie åè½å±ç¤º
slug: /gta5/lexis/lua/paid/reverie/show
---

<article><div class="theme-doc-markdown markdown"><header><h1 class="anchor anchorTargetStickyNavbar_Vzrq" id="reverie-åè½å±ç¤º">Reverie åè½å±ç¤º</h1></header>
<p><strong><span class="text-grey">èååè½å¾åä»ç»</span></strong></p>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="list"><strong>èååè¡¨</strong><a aria-label="listçç´æ¥é¾æ¥" class="hash-link" href="#list" title="listçç´æ¥é¾æ¥" translate="no">â</a></h2>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="details"><strong>èååè½å¾</strong><a aria-label="detailsçç´æ¥é¾æ¥" class="hash-link" href="#details" title="detailsçç´æ¥é¾æ¥" translate="no">â</a></h2>
<!-- -->
<section aria-label="Reverie äº¤äºå¼åè½å¾" class="preview_BkV3"><div class="heading_NGFL"><div class="identity_MO3c"><img alt="" height="30" loading="lazy" src="https://pic1.imgdb.cn/i/034sqGDwEs3vfu6BaeKWVw.png" width="30"/><div><strong>Reverie Lua</strong><span>ç¹å»åè½å³å¯é¢è§ Â· æ¯æä¸­è±åæ¢</span></div></div><button type="button">éç½®é¢è§</button></div><iframe class="frame_tzs9" loading="lazy" sandbox="allow-scripts" scrolling="no" srcdoc="&lt;!doctype html&gt;
&lt;html lang=&quot;zh-CN&quot;&gt;
&lt;head&gt;
&lt;meta charset=&quot;utf-8&quot;&gt;
&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1&quot;&gt;
&lt;title&gt;Reverie Lua äº¤äºå¼åè½é¢è§&lt;/title&gt;
&lt;style&gt;
/* ============================================================================
   REVERIE UI Â· 1:1 HTML replica of the Reverie.lua in-game menu
   All sizes are the raw `u(px)` values from Reverie.lua at scale = 1.
   ========================================================================== */

:root{
  --panel: 16, 17, 21;
  --text: 236, 237, 242;
  --dim: 152, 155, 165;
  --faint: 106, 109, 120;
  --white: 255, 255, 255;
  --green: 74, 222, 128;
  --amber: 251, 191, 36;
  --red: 248, 113, 113;
  --line: 255, 255, 255;
  --accent: 112, 98, 255;
  --accent2: 86, 168, 255;
  --opacity: .75;
  --zoom: 1;
  --fit: 1;
  --font: &quot;Segoe UI&quot;, &quot;SF Pro Text&quot;, system-ui, -apple-system, &quot;Microsoft YaHei&quot;, Arial, sans-serif;
}

*{ box-sizing: border-box; margin: 0; padding: 0; }

html, body{
  height: 100%;
  background: #0a0b0f;
  overflow: hidden;
  font-family: var(--font);
  -webkit-font-smoothing: antialiased;
  user-select: none;
}

/* GTA-ish backdrop behind the menu window */
.scene{
  position: fixed;
  inset: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background:
    radial-gradient(60% 50% at 50% 20%, rgba(70, 80, 110, .35), transparent 70%),
    radial-gradient(40% 40% at 80% 80%, rgba(112, 98, 255, .12), transparent 70%),
    linear-gradient(180deg, #171a22, #0a0b0f 60%, #05060a);
}
.scene::after{
  content: &quot;&quot;;
  position: absolute;
  inset: 0;
  background-image: repeating-linear-gradient(180deg, rgba(255,255,255,.02) 0 1px, transparent 1px 3px);
  pointer-events: none;
  opacity: .5;
}

.stage{
  transform: scale(calc(var(--fit) * var(--zoom)));
  transform-origin: center center;
}

/* ------------------------------------------------------------------ window */
.win{
  position: relative;
  width: 820px;
  height: 630px;
  border-radius: 10px;
  background: rgba(var(--panel), var(--opacity));
  box-shadow:
    0 0 0 1px rgba(0, 0, 0, .45),
    0 6px 40px 12px rgba(0, 0, 0, .28),
    0 2px 10px rgba(0, 0, 0, .5);
  color: rgb(var(--text));
  transition: opacity .22s ease, transform .22s ease;
  will-change: opacity, transform;
}
.win.closed{ opacity: 0; transform: scale(.97); pointer-events: none; }
.win::before{ /* inner top highlight */
  content: &quot;&quot;;
  position: absolute;
  left: 14px; right: 14px; top: 1px;
  height: 1px;
  background: rgba(var(--white), .06);
  border-radius: 2px;
  pointer-events: none;
}

/* accent bar on very top */
.topbar{
  position: absolute;
  left: 0; right: 0; top: 0;
  height: 2px;
  border-radius: 10px 10px 1px 1px;
  overflow: hidden;
  background: rgba(var(--accent), .95);
}
.topbar::after{
  content: &quot;&quot;;
  position: absolute;
  inset: 0 45% 0 0;
  background: rgba(var(--accent2), .55);
}
body.rainbow .topbar{
  background: linear-gradient(90deg, #ff5c5c, #ffa840, #fae248, #76f06e, #5ce8dc, #60acff, #b084ff, #ff78d6, #ff5c5c);
  background-size: 200% 100%;
  animation: rainbowSlide 3.4s linear infinite;
}
@keyframes rainbowSlide{ from{ background-position: 0 0 } to{ background-position: 200% 0 } }

/* ------------------------------------------------------------------ header */
.hdr{
  position: absolute;
  left: 0; right: 0; top: 2px;
  height: 62px;
  cursor: grab;
}
.hdr:active{ cursor: grabbing; }
.hdr .name{
  position: absolute;
  left: 20px; top: 14px;
  font-size: 15.5px;
  font-weight: 700;
  letter-spacing: .01em;
}
.hdr .sub{
  position: absolute;
  left: 20px; top: 35px;
  font-size: 9.5px;
  color: rgb(var(--faint));
}
.hdr .keycap{
  position: absolute;
  right: 54px; top: 22px;
  height: 20px;
  min-width: 34px;
  padding: 0 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 5px;
  background: rgba(var(--white), .07);
  box-shadow: inset 0 1px 0 rgba(var(--white), .05);
  font-size: 9.5px;
  font-weight: 700;
  color: rgb(var(--faint));
  letter-spacing: .06em;
}
/* è¯­è¨åæ¢æé®ï¼é¢å¤çä¾¿æ·å¥å£ï¼ä½ç½®å¨é®å¸½å·¦ä¾§ï¼æ ·å¼æ²¿ç¨é®å¸½è¯­è¨ï¼ */
.langbtn{
  position: absolute;
  right: 110px; top: 22px;
  height: 20px;
  padding: 2px;
  display: flex;
  align-items: center;
  gap: 1px;
  border: 0;
  border-radius: 5px;
  background: rgba(var(--white), .07);
  box-shadow: inset 0 1px 0 rgba(var(--white), .05);
  cursor: pointer;
  transition: background .15s;
}
.langbtn .lg{
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 22px;
  height: 16px;
  padding: 0 5px;
  border-radius: 4px;
  font-family: var(--font);
  font-size: 9px;
  font-weight: 700;
  letter-spacing: .06em;
  color: rgb(var(--faint));
  transition: background .15s, color .15s;
}
.langbtn:hover .lg{ color: rgb(var(--dim)); }
.langbtn .lg.on{ background: rgba(var(--accent), .8); color: #fff; }
.langbtn:active{ transform: translateY(1px); }

.hdr .close{
  position: absolute;
  right: 16px; top: 19px;
  width: 24px; height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 5px;
  border: 0;
  background: transparent;
  color: rgb(var(--faint));
  cursor: pointer;
  transition: background .15s, color .15s;
}
.hdr .close:hover{ background: rgba(var(--red), .16); color: rgb(var(--red)); }
.hdr .close svg{ width: 10px; height: 10px; }
.hdr-line{
  position: absolute;
  left: 0; right: 0; top: 64px;
  height: 1px;
  background: rgba(var(--white), .063);
}

/* ----------------------------------------------------------------- sidebar */
.side{
  position: absolute;
  left: 0; top: 64px;
  width: 206px;
  bottom: 34px;
  background: rgba(var(--white), .02);
  border-right: 1px solid rgba(var(--white), .057);
  overflow: hidden;
}
.tabs{
  position: absolute;
  left: 0; right: 0; top: 14px;
  display: flex;
  flex-direction: column;
  gap: 1px;
}
.tab{
  position: relative;
  height: 33px;
  margin: 0 8px;
  border: 0;
  border-radius: 6px;
  background: transparent;
  color: rgb(var(--dim));
  font: inherit;
  font-size: 12px;
  text-align: left;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 9px;
  padding: 0 13px;
  transition: background .16s ease, color .16s ease;
}
.tab svg{ width: 11px; height: 11px; color: rgb(var(--faint)); flex: none; transition: color .16s; }
.tab:hover{ background: rgba(var(--white), .04); }
.tab.sel{ background: rgba(var(--accent), .12); color: #fff; font-weight: 700; }
.tab.sel svg{ color: rgb(var(--accent)); }
.tab.sel::before{
  content: &quot;&quot;;
  position: absolute;
  left: 1px; top: 50%;
  transform: translateY(-50%);
  width: 2px; height: 17px;
  border-radius: 1px;
  background: rgb(var(--accent));
}
body.no-icons .tab svg{ display: none; }

.acct{
  position: absolute;
  left: 0; right: 0; bottom: 0;
  height: 48px;
  border-top: 1px solid rgba(var(--white), .045);
}
.acct .cap{
  position: absolute;
  left: 16px; top: 8px;
  font-size: 8.5px;
  font-weight: 700;
  letter-spacing: .14em;
  color: rgb(var(--faint));
}
.acct .user{
  position: absolute;
  left: 16px; top: 21px;
  font-size: 11.5px;
  font-weight: 700;
  color: rgb(var(--dim));
}
.acct .ver{
  position: absolute;
  right: 16px; top: 21px;
  font-size: 9.5px;
  color: rgb(var(--faint));
}

/* ----------------------------------------------------------------- content */
.view{
  position: absolute;
  left: 206px; right: 0; top: 64px;
  height: 532px;
  overflow: hidden;
}
.paper{
  position: absolute;
  left: 22px; top: 20px;
  width: 566px;
  will-change: transform;
}
.page-title{ font-size: 17.5px; font-weight: 700; line-height: 20px; }
.page-desc{ margin-top: 3px; font-size: 10.5px; line-height: 14px; color: rgb(var(--faint)); }
.page-desc:empty{ display: none; }
.page-line{ margin-top: 9px; height: 1px; background: rgba(var(--white), .063); }
.rows{ margin-top: 14px; }

.scrollbar{
  position: absolute;
  right: 6px; top: 8px;
  width: 2px;
  border-radius: 1px;
  background: rgba(var(--white), .18);
  opacity: 0;
  transition: opacity .2s;
}
.view.scrolling .scrollbar{ opacity: 1; }

/* ------------------------------------------------------------------- rows */
.row{
  position: relative;
  border-radius: 6px;
  cursor: pointer;
  transition: background .14s ease;
}
.row:hover{ background: rgba(var(--white), .035); }
.row.plain{ cursor: default; }
.row.plain:hover{ background: transparent; }

/* toggle */
.row.toggle .label{
  position: absolute;
  left: 0; right: 40px;
  font-size: 12.5px;
  font-weight: 700;
  line-height: 22px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.row.toggle.has-desc .label{ top: 2px; right: 40px; }
.row.toggle .desc{
  position: absolute;
  left: 0; top: 23px; right: 40px;
  height: 18px;
  font-size: 9.8px;
  line-height: 18px;
  color: rgb(var(--faint));
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.row.toggle .label.center{ top: 50%; transform: translateY(-50%); line-height: 18px; }
.tgl{
  position: absolute;
  right: 0; top: 50%;
  transform: translateY(-50%);
  width: 17px; height: 17px;
  border-radius: 4px;
  background: rgba(var(--white), .063);
  transition: background .18s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}
.tgl svg{ width: 9.5px; height: 9.5px; color: #fff; opacity: 0; transition: opacity .18s ease; }
.row.on .tgl{ background: rgb(var(--accent)); }
.row.on .tgl svg{ opacity: 1; }
body.no-icons .tgl svg{ display: none; }

/* slider */
.row.slider{ cursor: default; }
.row.slider .label{ font-size: 12.5px; line-height: 26px; }
.row.slider .val{
  position: absolute;
  right: 0; top: 0;
  font-size: 11.5px;
  font-weight: 700;
  line-height: 26px;
  color: rgb(var(--faint));
  transition: color .15s;
}
.row.slider:hover .val{ color: rgb(var(--dim)); }
.row.slider.drag .val{ color: rgb(var(--accent)); }
.track{
  position: absolute;
  left: 6px; right: 6px;
  bottom: 8px;
  height: 3px;
  border-radius: 1.5px;
  background: rgba(var(--white), .12);
}
.track .fill{
  position: absolute;
  left: 0; top: 0; bottom: 0;
  border-radius: 1.5px;
  background: rgba(var(--accent), .95);
}
.knob{
  position: absolute;
  top: 50%;
  width: 6px; height: 6px;
  margin: -3px 0 0 -3px;
  border-radius: 50%;
  background: #fff;
  box-shadow: 0 0 0 2px rgba(var(--accent), .16);
  transition: box-shadow .15s;
}
.row.slider:hover .knob{ box-shadow: 0 0 0 2px rgba(var(--accent), .24); }
.row.slider.drag .knob{ box-shadow: 0 0 0 2px rgba(var(--accent), .38); }

/* combo */
.row.combo .label{ font-size: 12.5px; line-height: 100%; position: absolute; top: 50%; transform: translateY(-50%); }
.row.combo .val{
  position: absolute;
  right: 19px; top: 50%;
  transform: translateY(-50%);
  font-size: 11.5px;
  font-weight: 700;
  color: rgb(var(--dim));
  max-width: 55%;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.row.combo .caret{
  position: absolute;
  right: 0; top: 50%;
  transform: translateY(-50%);
  width: 9px; height: 9px;
  color: rgb(var(--faint));
}
body.no-icons .row.combo .caret{ display: none; }
body.no-icons .row.combo .val{ right: 4px; }

/* button */
.btn{
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  border-radius: 6px;
  background: rgba(var(--white), .035);
  color: rgb(var(--text));
  font: inherit;
  font-size: 12px;
  font-weight: 700;
  border: 0;
  cursor: pointer;
  transition: background .15s, transform .08s;
  width: 100%;
}
.btn:hover{ background: rgba(var(--white), .085); }
.btn:active{ transform: translateY(1px); }
.btn svg{ width: 11px; height: 11px; color: rgb(var(--faint)); }
.btn.accent{ background: rgba(var(--accent), .88); color: #fff; }
.btn.accent svg{ color: #fff; }
.btn.accent:hover{ background: rgb(var(--accent)); }
.btn.danger{ background: rgba(var(--red), .086); color: rgb(var(--red)); }
.btn.danger svg{ color: rgb(var(--red)); }
.btn.danger:hover{ background: rgba(var(--red), .16); }
body.no-icons .btn svg{ display: none; }
.btnrow{ display: flex; gap: 10px; height: 100%; }
.btnrow .btn{ flex: 1 1 0; min-width: 0; }

/* multi field row (coordinates, clothing matrix) */
.flexbox{ display: flex; gap: 10px; align-items: center; }
.field{ position: relative; height: 100%; min-width: 0; }
.field input{
  position: absolute;
  left: 0; right: 0;
  top: 3px; bottom: 4px;
  width: 100%;
  border: 0; outline: 0; background: transparent;
  color: rgb(var(--text));
  font: inherit;
  font-size: 12px;
  caret-color: rgb(var(--accent));
}
.field .flab{
  position: absolute;
  left: 0; top: -2px;
  font-size: 9px;
  color: rgb(var(--faint));
  z-index: 1;
}
.field .uline{
  position: absolute;
  left: 0; right: 0; bottom: 3px;
  height: 1.2px;
  background: rgba(var(--white), .118);
  transition: background .18s;
}
.field.focus .uline{ background: rgb(var(--accent)); }

.cloth{ display: flex; flex-direction: column; gap: 2px; }
.clothrow{ display: flex; align-items: center; gap: 8px; }
.clothrow .nm{
  width: 62px;
  flex: none;
  font-size: 10px;
  color: rgb(var(--faint));
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.clothrow .field{ flex: 1 1 0; }

/* keybind */
.row.keybind .label{ font-size: 12.5px; line-height: 100%; position: absolute; top: 50%; transform: translateY(-50%); }
.keycap{
  position: absolute;
  right: 0; top: 50%;
  transform: translateY(-50%);
  min-width: 34px;
  height: 21px;
  padding: 0 9px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 5px;
  background: rgba(var(--white), .07);
  box-shadow: inset 0 1px 0 rgba(var(--white), .05);
  font-size: 10.5px;
  font-weight: 700;
  color: rgb(var(--dim));
}
.row.keybind.listen .keycap{
  background: rgba(var(--accent), .18);
  color: rgb(var(--accent));
  animation: keyPulse 1s ease-in-out infinite;
}
@keyframes keyPulse{ 0%,100%{ background: rgba(var(--accent), .18) } 50%{ background: rgba(var(--accent), .3) } }

/* textbox */
.row.textbox .lab{
  position: absolute;
  left: 0; top: 50%;
  transform: translateY(-50%);
  font-size: 10px;
  color: rgb(var(--faint));
}
.row.textbox input{
  position: absolute;
  left: 46px; right: 0;
  top: 0; bottom: 4px;
  width: calc(100% - 46px);
  border: 0;
  outline: 0;
  background: transparent;
  color: rgb(var(--text));
  font: inherit;
  font-size: 12.5px;
  caret-color: rgb(var(--accent));
}
.row.textbox .uline{
  position: absolute;
  left: 0; right: 0; bottom: 3px;
  height: 1.2px;
  background: rgba(var(--white), .118);
  transition: background .18s;
}
.row.textbox.focus .uline{ background: rgb(var(--accent)); }

/* info row */
.row.info .label{ font-size: 10.5px; line-height: 100%; position: absolute; top: 50%; transform: translateY(-50%); color: rgb(var(--faint)); }
.row.info .right{ position: absolute; right: 0; top: 50%; transform: translateY(-50%); font-size: 10.5px; font-weight: 700; color: rgb(var(--dim)); }

/* icon row */
.row.item .ic{ position: absolute; left: 0; top: 50%; transform: translateY(-50%); width: 10.5px; height: 10.5px; color: rgb(var(--faint)); }
.row.item .label{ position: absolute; left: 20px; top: 50%; transform: translateY(-50%); font-size: 12px; }
.row.item .right{ position: absolute; right: 0; top: 50%; transform: translateY(-50%); font-size: 10px; color: rgb(var(--faint)); }
.row.item:hover .ic{ color: rgb(var(--accent)); }
body.no-icons .row.item .label{ left: 0; }
body.no-icons .row.item .ic{ display: none; }

/* section */
.section{
  position: relative;
  display: flex;
  align-items: center;
  gap: 0;
  margin-top: 14px;
  height: 17px;
  margin-bottom: 6px;
  pointer-events: none;
}
.section svg{ width: 9.5px; height: 9.5px; color: rgb(var(--faint)); margin-right: 6px; }
.section .cap{ font-size: 9.8px; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; color: rgb(var(--dim)); }
.section .rule{ flex: 1; height: 1px; background: rgba(var(--white), .063); margin-left: 12px; }
body.no-icons .section svg{ display: none; }

/* home hero card */
.hero{
  position: relative;
  height: 88px;
  border-radius: 8px;
  background: rgba(var(--white), .02);
  box-shadow: inset 0 1px 0 rgba(var(--white), .05);
  cursor: default;
}
.hero::before{ content: &quot;&quot;; position: absolute; left: 0; top: 0; bottom: 0; width: 2px; border-radius: 1px; background: rgba(var(--accent), .9); }
.hero .n{ position: absolute; left: 18px; top: 14px; font-size: 20px; font-weight: 700; }
.hero .s{ position: absolute; left: 18px; top: 40px; font-size: 9.8px; color: rgb(var(--faint)); letter-spacing: .04em; text-transform: uppercase; }
.hero .badges{ position: absolute; left: 18px; top: 58px; display: flex; gap: 6px; }
.badge{
  height: 19px;
  padding: 0 9px;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  border-radius: 4px;
  font-size: 9.5px;
  font-weight: 700;
  letter-spacing: .1em;
  text-transform: uppercase;
}
.badge svg{ width: 9.5px; height: 9.5px; }
.badge.a{ background: rgba(var(--accent), .14); color: rgb(var(--accent)); }
.badge.b{ background: rgba(var(--accent2), .14); color: rgb(var(--accent2)); }
.badge.g{ background: rgba(var(--green), .14); color: rgb(var(--green)); }
body.no-icons .badge svg{ display: none; }

/* colour palette (ESP) */
.pal .lab{ font-size: 11px; line-height: 13px; color: rgb(var(--text)); }
.pal .cells{ position: absolute; left: 0; right: 0; top: 15px; display: grid; grid-template-columns: repeat(6, 1fr); gap: 3px 2px; }
.pal .cell{ height: 16px; border-radius: 3px; cursor: pointer; position: relative; }
.pal .cell.on::before{ content: &quot;&quot;; position: absolute; left: -1px; right: -1px; top: -1px; height: 1.8px; background: rgba(var(--white), .95); }
.pal .cell.on::after{ content: &quot;&quot;; position: absolute; left: -1px; right: -1px; bottom: -1px; height: 1.8px; background: rgba(var(--white), .95); }

/* ESP two-column layout */
.twocol{ display: flex; gap: 16px; position: relative; }
.twocol .col{ width: 275px; position: relative; }
.twocol .divider{ position: absolute; left: 283px; top: 0; width: 1px; background: rgba(var(--white), .063); }

/* chat */
.row.chat{ display: flex; align-items: center; gap: 8px; font-size: 11px; cursor: default; }
.row.chat .t{ font-size: 9.5px; color: rgb(var(--faint)); flex: none; }
.row.chat .n{ font-size: 11px; font-weight: 700; color: rgb(var(--dim)); flex: none; }
.row.chat .b{ font-size: 11px; color: rgb(var(--dim)); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.row.chat.me .n{ color: rgb(var(--accent2)); }
.row.chat.me .b{ color: rgb(var(--text)); }

/* ------------------------------------------------------------------ footer */
.foot{
  position: absolute;
  left: 0; right: 0; bottom: 0;
  height: 34px;
  border-top: 1px solid rgba(var(--white), .045);
  font-size: 9.5px;
  color: rgb(var(--faint));
}
.foot .l{ position: absolute; left: 20px; top: 50%; transform: translateY(-50%); }
.foot .r{ position: absolute; right: 20px; top: 50%; transform: translateY(-50%); }

/* ----------------------------------------------------------------- dropdown */
.dropdown{
  position: absolute;
  z-index: 40;
  padding: 4px 0;
  border-radius: 7px;
  background: rgba(22, 23, 28, .85);
  box-shadow:
    0 0 0 1px rgba(0, 0, 0, .4),
    0 10px 30px rgba(0, 0, 0, .5),
    inset 0 1px 0 rgba(var(--white), .06);
  max-height: 260px;
  overflow-y: auto;
  scrollbar-width: thin;
}
.dropdown::-webkit-scrollbar{ width: 2px; }
.dropdown::-webkit-scrollbar-thumb{ background: rgba(var(--accent), .55); }
.dd-item{
  position: relative;
  height: 29px;
  padding: 0 13px;
  display: flex;
  align-items: center;
  font-size: 11.5px;
  color: rgb(var(--dim));
  cursor: pointer;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.dd-item:hover{ background: rgba(var(--white), .06); color: rgb(var(--text)); }
.dd-item.sel{ color: rgb(var(--text)); font-weight: 700; }
.dd-item.sel::before{ content: &quot;&quot;; position: absolute; left: 5px; top: 7px; bottom: 7px; width: 2px; border-radius: 1px; background: rgb(var(--accent)); }

/* ------------------------------------------------------------------- toast */
.toasts{
  position: absolute;
  right: 24px; bottom: 22px;
  width: 272px;
  display: flex;
  flex-direction: column-reverse;
  gap: 6px;
  z-index: 60;
  pointer-events: none;
}
.toast{
  height: 50px;
  border-radius: 8px;
  background: rgba(22, 23, 28, .9);
  box-shadow: 0 0 0 1px rgba(var(--white), .06), 0 12px 26px rgba(0, 0, 0, .45);
  padding: 0 14px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  animation: toastIn .22s ease both;
  overflow: hidden;
}
.toast.out{ animation: toastOut .2s ease both; }
.toast .tt{ font-size: 11.5px; font-weight: 700; color: rgb(var(--text)); }
.toast .td{ font-size: 9.5px; color: rgb(var(--faint)); margin-top: 2px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.toast .bar{ position: absolute; left: 0; top: 0; bottom: 0; width: 2px; background: rgb(var(--accent)); }
.toast.ok .bar{ background: rgb(var(--green)); }
.toast.warn .bar{ background: rgb(var(--amber)); }
.toast.err .bar{ background: rgb(var(--red)); }
@keyframes toastIn{ from{ opacity: 0; transform: translateX(16px) } to{ opacity: 1; transform: none } }
@keyframes toastOut{ from{ opacity: 1 } to{ opacity: 0; transform: translateX(16px) } }

/* debug overlay */
.debug{
  position: fixed;
  left: 12px; top: 12px;
  font: 11px/1.5 ui-monospace, Consolas, monospace;
  color: #9ad0ff;
  background: rgba(0, 0, 0, .5);
  padding: 8px 10px;
  border-radius: 6px;
  display: none;
  z-index: 100;
}
body.debug-on .debug{ display: block; }

/* re-open hint (only when the window is closed) */
.hint{
  position: fixed;
  left: 50%; bottom: 28px;
  transform: translateX(-50%);
  font-size: 12px;
  letter-spacing: .18em;
  color: rgba(235, 240, 250, .45);
  text-transform: uppercase;
  display: none;
  pointer-events: none;
}
body.win-closed .hint{ display: block; }

/* Fit the original menu directly to the embedded viewport. */
.scene { display: block; }
.stage { width: 100%; transform: none; }
.win { width: 100%; height: 630px; border-radius: 0; box-shadow: none; }
.paper { width: calc(100% - 44px); }
.hint { bottom: 24px; cursor: pointer; pointer-events: auto; }
.tabs {
  bottom: 52px;
  overflow-y: auto;
  overscroll-behavior: contain;
  scrollbar-width: thin;
  scrollbar-color: #46444f #15151c;
}
.tabs::-webkit-scrollbar { width: 4px; height: 4px; }
.tabs::-webkit-scrollbar-track { background: #15151c; }
.tabs::-webkit-scrollbar-thumb { background: #46444f; border-radius: 4px; }
.tabs::-webkit-scrollbar-thumb:hover { background: #696575; }
.tabs::-webkit-scrollbar-corner { background: #15151c; }
.tabs .tab { flex-shrink: 0; }
.row.slider { touch-action: pan-y; }
.dropdown { overflow-y: auto; overscroll-behavior: contain; }
@media (max-width: 650px) {
  .win { height: 684px; }
  .side {
    left: 0; right: 0; top: 64px;
    width: auto; height: 54px;
    border-right: 0;
    border-bottom: 1px solid rgba(var(--white), .05);
  }
  .tabs {
    top: 7px; bottom: 7px;
    flex-direction: row;
    gap: 4px;
    padding: 0 8px;
    overflow-x: auto;
    overflow-y: hidden;
  }
  .tab { height: 38px; padding: 0 12px; margin: 0; white-space: nowrap; }
  .acct { display: none; }
  .view { top: 118px; left: 0; height: 532px; }
  .paper { left: 16px; width: calc(100% - 32px); }
  .twocol { flex-direction: column; }
  .twocol .col { width: 100%; min-width: 0; flex: none; }
  .twocol .divider { display: none; }
  .btnrow { gap: 6px; }
  .btn { padding: 0 4px; font-size: 11px; }
  .row.combo .label { max-width: 48%; line-height: 1.3; }
  .row .desc { white-space: normal; }
  .row.has-desc { min-height: 56px; }
  .foot .l { font-size: 8px; }
}

&lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;

&lt;div class=&quot;scene&quot;&gt;
  &lt;div class=&quot;stage&quot; id=&quot;stage&quot;&gt;
    &lt;div class=&quot;win&quot; id=&quot;win&quot;&gt;

      &lt;div class=&quot;topbar&quot;&gt;&lt;/div&gt;

      &lt;div class=&quot;hdr&quot; id=&quot;hdr&quot;&gt;
        &lt;div class=&quot;name&quot;&gt;Reverie&lt;/div&gt;
        &lt;div class=&quot;sub&quot; id=&quot;hdrSub&quot;&gt;reverie v0.4&lt;/div&gt;
        &lt;div class=&quot;keycap&quot; id=&quot;hdrKey&quot;&gt;INSERT&lt;/div&gt;
        &lt;button class=&quot;langbtn&quot; id=&quot;langBtn&quot; type=&quot;button&quot; title=&quot;åæ¢è¯­è¨ / Switch language&quot; aria-label=&quot;Switch language&quot;&gt;
          &lt;span class=&quot;lg&quot; data-lang=&quot;en&quot;&gt;EN&lt;/span&gt;&lt;span class=&quot;lg&quot; data-lang=&quot;zh&quot;&gt;ä¸­&lt;/span&gt;
        &lt;/button&gt;
        &lt;button class=&quot;close&quot; id=&quot;close&quot; type=&quot;button&quot; aria-label=&quot;Close&quot;&gt;
          &lt;svg viewBox=&quot;0 0 24 24&quot; fill=&quot;currentColor&quot; aria-hidden=&quot;true&quot;&gt;
            &lt;path d=&quot;M6.2 6.2a1 1 0 0 1 1.4 0L12 10.6l4.4-4.4a1 1 0 1 1 1.4 1.4L13.4 12l4.4 4.4a1 1 0 0 1-1.4 1.4L12 13.4l-4.4 4.4a1 1 0 0 1-1.4-1.4l4.4-4.4-4.4-4.4a1 1 0 0 1 0-1.4Z&quot;/&gt;
          &lt;/svg&gt;
        &lt;/button&gt;
      &lt;/div&gt;
      &lt;div class=&quot;hdr-line&quot;&gt;&lt;/div&gt;

      &lt;div class=&quot;side&quot;&gt;
        &lt;div class=&quot;tabs&quot; id=&quot;tabs&quot;&gt;&lt;/div&gt;
        &lt;div class=&quot;acct&quot;&gt;
          &lt;div class=&quot;cap&quot; id=&quot;acctCap&quot;&gt;ACCOUNT&lt;/div&gt;
          &lt;div class=&quot;user&quot;&gt;Reverie&lt;/div&gt;
          &lt;div class=&quot;ver&quot;&gt;0.4&lt;/div&gt;
        &lt;/div&gt;
      &lt;/div&gt;

      &lt;div class=&quot;view&quot; id=&quot;view&quot;&gt;
        &lt;div class=&quot;paper&quot; id=&quot;paper&quot;&gt;&lt;/div&gt;
        &lt;div class=&quot;scrollbar&quot; id=&quot;scrollbar&quot;&gt;&lt;/div&gt;
      &lt;/div&gt;

      &lt;div class=&quot;foot&quot;&gt;
        &lt;span class=&quot;l&quot; id=&quot;footLeft&quot;&gt;click Â· drag header Â· wheel scroll&lt;/span&gt;
        &lt;span class=&quot;r&quot;&gt;Reverie 0.4&lt;/span&gt;
      &lt;/div&gt;

      &lt;div class=&quot;toasts&quot; id=&quot;toasts&quot;&gt;&lt;/div&gt;
    &lt;/div&gt;
  &lt;/div&gt;
&lt;/div&gt;

&lt;div class=&quot;hint&quot; id=&quot;hint&quot;&gt;press INSERT to re-open&lt;/div&gt;
&lt;div class=&quot;debug&quot; id=&quot;debug&quot;&gt;&lt;/div&gt;

&lt;script&gt;
/* REVERIE UI Â· page model â generated from Reverie.lua (Powers page excluded) */
window.REVERIE_LISTS = {
 &quot;espPalette&quot;: [
  [
   255,
   92,
   92
  ],
  [
   255,
   168,
   64
  ],
  [
   250,
   226,
   72
  ],
  [
   118,
   240,
   110
  ],
  [
   92,
   232,
   220
  ],
  [
   96,
   172,
   255
  ],
  [
   176,
   132,
   255
  ],
  [
   255,
   120,
   214
  ],
  [
   240,
   240,
   245
  ],
  [
   152,
   158,
   176
  ],
  [
   44,
   48,
   58
  ],
  [
   132,
   255,
   160
  ]
 ],
 &quot;accents&quot;: [
  &quot;Indigo&quot;,
  &quot;Cyan&quot;,
  &quot;Emerald&quot;,
  &quot;Amber&quot;,
  &quot;Rose&quot;
 ]
};
window.REVERIE_PAGES = [
 {
  &quot;name&quot;: &quot;Home&quot;,
  &quot;title&quot;: &quot;Overview&quot;,
  &quot;icon&quot;: &quot;home&quot;,
  &quot;desc&quot;: &quot;Overview: session status, quick toggles and shortcuts. Tip: every feature lives in the sidebar on the left.&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;hero&quot;
   },
   {
    &quot;t&quot;: &quot;space&quot;,
    &quot;h&quot;: 12
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Session&quot;,
    &quot;icon&quot;: &quot;globe&quot;
   },
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 24,
    &quot;label&quot;: &quot;Player&quot;,
    &quot;right&quot;: &quot;Reverie&quot;
   },
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 24,
    &quot;label&quot;: &quot;Session id&quot;,
    &quot;right&quot;: &quot;12&quot;
   },
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 24,
    &quot;label&quot;: &quot;Rank&quot;,
    &quot;right&quot;: &quot;120&quot;
   }
  ]
 },
 {
  &quot;name&quot;: &quot;Self&quot;,
  &quot;title&quot;: &quot;Self&quot;,
  &quot;desc&quot;: &quot;Self: health, invisibility, fire fist, sword storm, spins, clothing, coordinates, weapons and a forward blink.&quot;,
  &quot;icon&quot;: &quot;user&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Protection&quot;,
    &quot;icon&quot;: &quot;skull&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Invisible&quot;,
    &quot;desc&quot;: &quot;Your character turns invisible to other players. Tip: switch it off in cutscenes or the camera may look odd.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 1
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Health&quot;,
    &quot;icon&quot;: &quot;heart&quot;
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Health&quot;,
    &quot;min&quot;: 100,
    &quot;max&quot;: 400,
    &quot;step&quot;: 10,
    &quot;fmt&quot;: &quot;%.0f&quot;,
    &quot;value&quot;: 200,
    &quot;gid&quot;: 2
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Armour&quot;,
    &quot;min&quot;: 0,
    &quot;max&quot;: 100,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0f&quot;,
    &quot;value&quot;: 100,
    &quot;gid&quot;: 3
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 36,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Apply stats&quot;,
      &quot;icon&quot;: &quot;check&quot;,
      &quot;style&quot;: &quot;accent&quot;
     },
     {
      &quot;label&quot;: &quot;Clear wanted&quot;,
      &quot;icon&quot;: &quot;skull&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Navigation&quot;,
    &quot;icon&quot;: &quot;globe&quot;
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 36,
    &quot;label&quot;: &quot;Teleport to waypoint&quot;,
    &quot;icon&quot;: &quot;pointer&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 5
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Self&quot;,
    &quot;icon&quot;: &quot;bolt&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Full health&quot;,
    &quot;desc&quot;: &quot;Health is refilled continuously. Tip: keep it on together with Half god.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 6
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Half god&quot;,
    &quot;desc&quot;: &quot;You take almost no damage. Tip: heavy explosions can still hurt; use Lightless shield for those.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 7
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Invincible&quot;,
    &quot;desc&quot;: &quot;No damage from bullets, fire, explosions, melee or drowning. Tip: turn it off when a mission needs you to die.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 8
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Flash speed&quot;,
    &quot;min&quot;: 1,
    &quot;max&quot;: 15,
    &quot;step&quot;: 0.5,
    &quot;fmt&quot;: &quot;%.1fx&quot;,
    &quot;value&quot;: 1,
    &quot;gid&quot;: 9
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Flash&quot;,
    &quot;desc&quot;: &quot;Multiplies your sprint speed only (walking stays normal).&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 10
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Bunny hop&quot;,
    &quot;desc&quot;: &quot;Hold Space to jump continuously; hold Shift too to build speed with each jump.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 11
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Speed cap&quot;,
    &quot;min&quot;: 10,
    &quot;max&quot;: 300,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0f m/s&quot;,
    &quot;value&quot;: 60,
    &quot;gid&quot;: 12
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Water walk&quot;,
    &quot;desc&quot;: &quot;Walk on water. Tip: keep it off when you want to swim down, it holds you on the surface.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 14
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Weapon&quot;,
    &quot;icon&quot;: &quot;fire&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Rainbow gun&quot;,
    &quot;desc&quot;: &quot;Your weapons cycle through rainbow colours. Tip: works on ranged weapons you already own.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 15
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Laser eyes&quot;,
    &quot;desc&quot;: &quot;Shoots wherever you look. Tip: fire with X only, and pick the version below.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 16
   },
   {
    &quot;t&quot;: &quot;combo&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;Laser version&quot;,
    &quot;items&quot;: [
     &quot;V1&quot;,
     &quot;V2&quot;,
     &quot;V3&quot;
    ],
    &quot;idx&quot;: 0,
    &quot;gid&quot;: 17
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Physics&quot;,
    &quot;icon&quot;: &quot;skull&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Fire fist&quot;,
    &quot;desc&quot;: &quot;Fist of fire. Tip: hold RMB to charge, then LMB to punch out a flame; fists only, and no charge means no fire.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 18
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Lightless shield&quot;,
    &quot;desc&quot;: &quot;Anyone touching you is blown away by an invisible blast.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 19
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Sword storm&quot;,
    &quot;desc&quot;: &quot;Swords fly out from you to cut down nearby NPCs and empty vehicles. Tip: Sword count and Attack range below set how many and how far.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 20
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Local swords&quot;,
    &quot;desc&quot;: &quot;Turn this on if the swords do not show up. Off = normal mode.&quot;,
    &quot;on&quot;: true,
    &quot;gid&quot;: 21
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Sword count&quot;,
    &quot;min&quot;: 10,
    &quot;max&quot;: 30,
    &quot;step&quot;: 1,
    &quot;fmt&quot;: &quot;%.0f&quot;,
    &quot;value&quot;: 10,
    &quot;gid&quot;: 22
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Attack range&quot;,
    &quot;min&quot;: 5,
    &quot;max&quot;: 100,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0f m&quot;,
    &quot;value&quot;: 30,
    &quot;gid&quot;: 23
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Sword damage&quot;,
    &quot;min&quot;: 1,
    &quot;max&quot;: 500,
    &quot;step&quot;: 1,
    &quot;fmt&quot;: &quot;%.0f&quot;,
    &quot;value&quot;: 10,
    &quot;gid&quot;: 24
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Sword rain&quot;,
    &quot;desc&quot;: &quot;Swords fall from the sky onto nearby targets.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 25
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Spin&quot;,
    &quot;desc&quot;: &quot;ä½ ç©è¿CSåï¼&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 26
   },
   {
    &quot;t&quot;: &quot;combo&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;Spin target&quot;,
    &quot;items&quot;: [
     &quot;NPCs&quot;,
     &quot;Players&quot;,
     &quot;NPCs + players&quot;,
     &quot;None&quot;
    ],
    &quot;idx&quot;: 0,
    &quot;gid&quot;: 27
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Big spin&quot;,
    &quot;desc&quot;: &quot;ä½ ç©è¿CSåï¼&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 28
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Big spin 1.6&quot;,
    &quot;desc&quot;: &quot;ä½ ç©è¿CSåï¼&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 29
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Karma&quot;,
    &quot;desc&quot;: &quot;Whoever aims at you gets blasted when you die.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 30
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Clothing&quot;,
    &quot;icon&quot;: &quot;user&quot;
   },
   {
    &quot;t&quot;: &quot;cloth&quot;,
    &quot;h&quot;: 22,
    &quot;items&quot;: [
     &quot;Head&quot;,
     &quot;Mask&quot;,
     &quot;Hair&quot;,
     &quot;Torso&quot;,
     &quot;Legs&quot;,
     &quot;Bag&quot;,
     &quot;Shoes&quot;,
     &quot;Accessory&quot;,
     &quot;Undershirt&quot;,
     &quot;Armor&quot;,
     &quot;Decals&quot;,
     &quot;Top&quot;
    ]
   },
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 24,
    &quot;label&quot;: &quot;Style&quot;,
    &quot;right&quot;: &quot;/&quot;
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Apply&quot;,
      &quot;icon&quot;: &quot;check&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Read current&quot;,
      &quot;icon&quot;: &quot;save&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Random&quot;,
      &quot;icon&quot;: &quot;star&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Save outfit&quot;,
      &quot;icon&quot;: &quot;save&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Wear outfit&quot;,
      &quot;icon&quot;: &quot;check&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Coordinates&quot;,
    &quot;icon&quot;: &quot;pointer&quot;
   },
   {
    &quot;t&quot;: &quot;coords&quot;,
    &quot;h&quot;: 34
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Teleport&quot;,
      &quot;icon&quot;: &quot;pointer&quot;,
      &quot;style&quot;: &quot;accent&quot;
     },
     {
      &quot;label&quot;: &quot;Read current&quot;,
      &quot;icon&quot;: &quot;save&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Weapons&quot;,
    &quot;icon&quot;: &quot;fire&quot;
   },
   {
    &quot;t&quot;: &quot;combo&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;Weapon&quot;,
    &quot;items&quot;: [
     &quot;weapon_pistol50&quot;,
     &quot;weapon_microsmg&quot;,
     &quot;weapon_carbinerifle&quot;,
     &quot;weapon_pumpshotgun&quot;,
     &quot;weapon_sniperrifle&quot;,
     &quot;weapon_grenadelauncher&quot;,
     &quot;weapon_rpg&quot;,
     &quot;weapon_minigun&quot;,
     &quot;weapon_railgun&quot;,
     &quot;weapon_stickybomb&quot;
    ],
    &quot;idx&quot;: 0,
    &quot;gid&quot;: 39
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Give weapon&quot;,
      &quot;icon&quot;: &quot;check&quot;,
      &quot;style&quot;: &quot;accent&quot;
     },
     {
      &quot;label&quot;: &quot;Give all&quot;,
      &quot;icon&quot;: &quot;plus&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Infinite ammo&quot;,
    &quot;desc&quot;: &quot;You never run out of reserve ammo.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 41
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;No reload&quot;,
    &quot;desc&quot;: &quot;Your magazines refill themselves.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 42
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Damage&quot;,
    &quot;min&quot;: 1,
    &quot;max&quot;: 10,
    &quot;step&quot;: 0.5,
    &quot;fmt&quot;: &quot;%.1fx&quot;,
    &quot;value&quot;: 1,
    &quot;gid&quot;: 43
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Mission&quot;,
    &quot;icon&quot;: &quot;check&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Skip cutscene&quot;,
    &quot;desc&quot;: &quot;Cutscenes are skipped automatically. Tip: keep it off in heists where a cutscene marks progress.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 44
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Blink forward&quot;,
    &quot;icon&quot;: &quot;rocket&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 45
   }
  ]
 },
 {
  &quot;name&quot;: &quot;Vehicle&quot;,
  &quot;title&quot;: &quot;Vehicle&quot;,
  &quot;desc&quot;: &quot;Vehicle: top speed, water driving, god mode, ghost mode, rainbow paint, neon and a vehicle spawner with max upgrades.&quot;,
  &quot;icon&quot;: &quot;car&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Vehicle&quot;,
    &quot;icon&quot;: &quot;bolt&quot;
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Repair now&quot;,
    &quot;icon&quot;: &quot;wrench&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 1
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Unlock top speed&quot;,
    &quot;desc&quot;: &quot;Lifts your vehicle speed limit a lot. Tip: hold forward and avoid tight corners at full speed.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 2
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Why didn't you tell me about such a fast car&quot;,
    &quot;desc&quot;: &quot;Why didn't you tell me about such a fast car sooner&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 3
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Vehicle god mode&quot;,
    &quot;desc&quot;: &quot;Your car cannot be wrecked by crashes or explosions.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 4
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Auto flip&quot;,
    &quot;desc&quot;: &quot;Flips the vehicle back upright when it ends up on its roof. Tip: handy for stunt driving.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 5
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Water driving&quot;,
    &quot;desc&quot;: &quot;Drives on water: the car floats on the surface instead of sinking. Tip: raise Float height if the car sits too low.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 6
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Float height&quot;,
    &quot;min&quot;: 0,
    &quot;max&quot;: 2,
    &quot;step&quot;: 0.1,
    &quot;fmt&quot;: &quot;%.1f m&quot;,
    &quot;value&quot;: 0.4,
    &quot;gid&quot;: 7
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Roadster&quot;,
    &quot;icon&quot;: &quot;bolt&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Instant torque&quot;,
    &quot;desc&quot;: &quot;Full torque from a standstill: brutal acceleration and a much higher top speed.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 8
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;SpaceX thrusters&quot;,
    &quot;desc&quot;: &quot;Cold-gas thrusters: hold TAB to launch forward, hold C to thrust backward, TAB+Space to jump straight up. Pressing TAB and C together does nothing.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 9
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Thrust power&quot;,
    &quot;min&quot;: 1,
    &quot;max&quot;: 10,
    &quot;step&quot;: 1,
    &quot;fmt&quot;: &quot;%.0fx&quot;,
    &quot;value&quot;: 2,
    &quot;gid&quot;: 10
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Unlimited thrusters&quot;,
    &quot;desc&quot;: &quot;Unlimited charge, unlimited thrust&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 11
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Regen braking&quot;,
    &quot;min&quot;: 0,
    &quot;max&quot;: 30,
    &quot;step&quot;: 1,
    &quot;fmt&quot;: &quot;%.0f m/s2&quot;,
    &quot;value&quot;: 9,
    &quot;gid&quot;: 12
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Grip&quot;,
    &quot;min&quot;: 0,
    &quot;max&quot;: 1,
    &quot;step&quot;: 0.05,
    &quot;fmt&quot;: &quot;%.2f&quot;,
    &quot;value&quot;: 0.6,
    &quot;gid&quot;: 13
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Summon vehicle&quot;,
    &quot;icon&quot;: &quot;car&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 14
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Flight&quot;,
    &quot;icon&quot;: &quot;bolt&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Fly vehicle&quot;,
    &quot;desc&quot;: &quot;Free flight. Tip: aim with the camera, WASD to fly, Space up and Ctrl down.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 15
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Fly speed&quot;,
    &quot;min&quot;: 5,
    &quot;max&quot;: 150,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0f&quot;,
    &quot;value&quot;: 40,
    &quot;gid&quot;: 16
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Rainbow&quot;,
    &quot;icon&quot;: &quot;star&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Rainbow paint&quot;,
    &quot;desc&quot;: &quot;Paint fades through a rainbow. Tip: only the driver's view changes instantly; passengers see the current colour.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 17
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Rainbow neon&quot;,
    &quot;desc&quot;: &quot;Neon fades through a rainbow. Tip: turn it off while you are only a passenger.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 18
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Disable as passenger&quot;,
    &quot;desc&quot;: &quot;Keeps the rainbow effects off while someone else drives. Tip: handy when riding with friends.&quot;,
    &quot;on&quot;: true,
    &quot;gid&quot;: 19
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Spawner&quot;,
    &quot;icon&quot;: &quot;plus&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Ghost car&quot;,
    &quot;desc&quot;: &quot;Your car passes straight through traffic and walls.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 20
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Max upgrades&quot;,
    &quot;icon&quot;: &quot;wrench&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 21
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;XML vehicle&quot;,
    &quot;icon&quot;: &quot;plus&quot;
   },
   {
    &quot;t&quot;: &quot;combo&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;XML file&quot;,
    &quot;items&quot;: [
     &quot;#ArmedETR1&quot;,
     &quot;aaaSHadowMechaV1&quot;,
     &quot;aaaWarBaseVehical&quot;,
     &quot;Apoc Penetrator 1.5&quot;,
     &quot;BIGHEAD AngryDog&quot;,
     &quot;BIGHEAD ArmoredMechanic&quot;,
     &quot;BIGHEAD Body Collector&quot;,
     &quot;BIGHEAD BurgerTruck&quot;,
     &quot;BIGHEAD Cinema Car&quot;,
     &quot;BIGHEAD CustomUFO2&quot;,
     &quot;BIGHEAD Dogsled2&quot;,
     &quot;BIGHEAD FutureBike2&quot;,
     &quot;BIGHEAD FutureBike3&quot;,
     &quot;BIGHEAD JuiceDump&quot;,
     &quot;BIGHEAD LightBike&quot;,
     &quot;BIGHEAD LightIssi&quot;,
     &quot;BIGHEAD MoneyMonster&quot;,
     &quot;BIGHEAD MurderCar&quot;,
     &quot;BIGHEAD ParagonTruck&quot;,
     &quot;BIGHEAD PurpleGangGunner&quot;,
     &quot;BIGHEAD RC Chop&quot;,
     &quot;BIGHEAD RC Ped&quot;,
     &quot;BIGHEAD RC Ramp&quot;,
     &quot;BIGHEAD SOLIDRAMP&quot;,
     &quot;BIGHEAD SOLIDSTUNTJUMP&quot;,
     &quot;BIGHEAD TrainBike&quot;,
     &quot;BIGHEAD UFO&quot;,
     &quot;BIGHEAD XMAS&quot;,
     &quot;Butcher Heli&quot;,
     &quot;Cargo Ship (Tugboat)&quot;,
     &quot;Hover Spaceship&quot;,
     &quot;Hoverbike&quot;,
     &quot;Katana-Mobile&quot;,
     &quot;NEON - Lowell&quot;,
     &quot;Neon - Osiris GT-500&quot;,
     &quot;NuclearRocket&quot;,
     &quot;Old Tank&quot;,
     &quot;Poolmobile (no peds)&quot;,
     &quot;Realistic ghost rider motorbike&quot;,
     &quot;RHINO TRON 2.0&quot;,
     &quot;Robot&quot;,
     &quot;ROBOT'1-SYXAPUK&quot;,
     &quot;ROBOT'2-SYXAPUK&quot;,
     &quot;ROBOT'3-SYXAPUK&quot;,
     &quot;Robot'4-Syxapuk&quot;,
     &quot;Rocket Ramp&quot;,
     &quot;Santa Car Xmas 2016 Edition&quot;,
     &quot;Spider&quot;,
     &quot;Subway&quot;,
     &quot;T20 Police&quot;,
     &quot;The Dreadnaught&quot;,
     &quot;TheFastFoliage&quot;,
     &quot;toutfeutoutflamme&quot;,
     &quot;Truck With Ramp&quot;,
     &quot;Ultimate Dozer&quot;,
     &quot;ZapperTruck&quot;,
     &quot;Zombie Plow&quot;,
     &quot;ZombieRanger&quot;
    ],
    &quot;idx&quot;: 0,
    &quot;gid&quot;: 22
   },
   {
    &quot;t&quot;: &quot;textbox&quot;,
    &quot;h&quot;: 36,
    &quot;label&quot;: &quot;Custom XML path&quot;,
    &quot;value&quot;: &quot;&quot;,
    &quot;gid&quot;: 23
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Spawn from XML&quot;,
    &quot;icon&quot;: &quot;car&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 24
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Spawned XML vehicles&quot;,
    &quot;icon&quot;: &quot;car&quot;
   },
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 24,
    &quot;label&quot;: &quot;No XML vehicle spawned yet&quot;,
    &quot;right&quot;: &quot;&quot;
   },
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 24,
    &quot;label&quot;: &quot;#&quot;,
    &quot;right&quot;: &quot;&quot;
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 26,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Teleport it to me&quot;,
      &quot;icon&quot;: &quot;&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Teleport to it&quot;,
      &quot;icon&quot;: &quot;&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Get in driver seat&quot;,
      &quot;icon&quot;: &quot;&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Delete&quot;,
      &quot;icon&quot;: &quot;trash&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   }
  ]
 },
 {
  &quot;name&quot;: &quot;World&quot;,
  &quot;title&quot;: &quot;World&quot;,
  &quot;desc&quot;: &quot;World: time of day and weather. Tip: pick a value, then press Apply (changing time online needs you to be host).&quot;,
  &quot;icon&quot;: &quot;globe&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Time&quot;,
    &quot;icon&quot;: &quot;clock&quot;
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Hour&quot;,
    &quot;min&quot;: 0,
    &quot;max&quot;: 23,
    &quot;step&quot;: 1,
    &quot;fmt&quot;: &quot;%02.0f:00&quot;,
    &quot;value&quot;: 12,
    &quot;gid&quot;: 1
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 36,
    &quot;label&quot;: &quot;Apply time&quot;,
    &quot;icon&quot;: &quot;clock&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 2
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Freeze clock&quot;,
    &quot;desc&quot;: &quot;Time of day stays where it is.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 3
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Weather&quot;,
    &quot;icon&quot;: &quot;globe&quot;
   },
   {
    &quot;t&quot;: &quot;combo&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;Type&quot;,
    &quot;items&quot;: [
     &quot;EXTRASUNNY&quot;,
     &quot;CLEAR&quot;,
     &quot;CLOUDS&quot;,
     &quot;OVERCAST&quot;,
     &quot;RAIN&quot;,
     &quot;CLEARING&quot;,
     &quot;THUNDER&quot;,
     &quot;SMOG&quot;,
     &quot;FOGGY&quot;,
     &quot;SNOW&quot;,
     &quot;BLIZZARD&quot;,
     &quot;XMAS&quot;,
     &quot;HALLOWEEN&quot;,
     &quot;NEUTRAL&quot;,
     &quot;SNOWLIGHT&quot;
    ],
    &quot;idx&quot;: 0,
    &quot;gid&quot;: 4
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 36,
    &quot;label&quot;: &quot;Apply weather&quot;,
    &quot;icon&quot;: &quot;bolt&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 5
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Lock weather&quot;,
    &quot;desc&quot;: &quot;éå®å¤©æ°&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 6
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 36,
    &quot;label&quot;: &quot;Summon lightning&quot;,
    &quot;icon&quot;: &quot;bolt&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 7
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Wind speed&quot;,
    &quot;min&quot;: 0,
    &quot;max&quot;: 30,
    &quot;step&quot;: 1,
    &quot;fmt&quot;: &quot;%.0f&quot;,
    &quot;value&quot;: 5,
    &quot;gid&quot;: 8
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Remove rain and snow&quot;,
    &quot;desc&quot;: &quot;å é¤é¨éª&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 9
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Clock&quot;,
    &quot;icon&quot;: &quot;clock&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Sync real time&quot;,
    &quot;desc&quot;: &quot;Keeps the in-game clock following your computer's local time.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 10
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Clock speed&quot;,
    &quot;min&quot;: 1,
    &quot;max&quot;: 60,
    &quot;step&quot;: 1,
    &quot;fmt&quot;: &quot;%.0fx&quot;,
    &quot;value&quot;: 1,
    &quot;gid&quot;: 11
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;NPC&quot;,
    &quot;icon&quot;: &quot;users&quot;
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Radius&quot;,
    &quot;min&quot;: 5,
    &quot;max&quot;: 200,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0f m&quot;,
    &quot;value&quot;: 25,
    &quot;gid&quot;: 12
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Kill NPCs&quot;,
      &quot;icon&quot;: &quot;skull&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Kill enemies&quot;,
      &quot;icon&quot;: &quot;skull&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Kill all NPCs&quot;,
      &quot;icon&quot;: &quot;skull&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Kill all enemies&quot;,
      &quot;icon&quot;: &quot;skull&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Delete nearby enemies&quot;,
      &quot;icon&quot;: &quot;trash&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Delete all enemies&quot;,
      &quot;icon&quot;: &quot;trash&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Auto kill NPCs&quot;,
    &quot;desc&quot;: &quot;Kills NPCs inside the radius every second.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 16
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Auto kill enemies&quot;,
    &quot;desc&quot;: &quot;Kills only NPCs that are fighting you, every second.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 17
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Remove bodies&quot;,
    &quot;icon&quot;: &quot;trash&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 18
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Give all weapons&quot;,
      &quot;icon&quot;: &quot;fire&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Remove weapons&quot;,
      &quot;icon&quot;: &quot;trash&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Environment&quot;,
    &quot;icon&quot;: &quot;globe&quot;
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Remove air defences&quot;,
    &quot;icon&quot;: &quot;warn&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 20
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Remove cameras&quot;,
    &quot;icon&quot;: &quot;eye&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 21
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Remove all cameras&quot;,
    &quot;icon&quot;: &quot;eye&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 22
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Soul&quot;,
    &quot;icon&quot;: &quot;eye&quot;
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Soul speed&quot;,
    &quot;min&quot;: 5,
    &quot;max&quot;: 200,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0f m/s&quot;,
    &quot;value&quot;: 25,
    &quot;gid&quot;: 23
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Out of body&quot;,
    &quot;desc&quot;: &quot;çµé­åºçª&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 24
   }
  ]
 },
 {
  &quot;name&quot;: &quot;Target&quot;,
  &quot;title&quot;: &quot;Target&quot;,
  &quot;icon&quot;: &quot;users&quot;,
  &quot;desc&quot;: &quot;&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Target&quot;,
    &quot;icon&quot;: &quot;user&quot;
   },
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 22,
    &quot;label&quot;: &quot;Select a player in Lexis â Online players, then come back.&quot;
   },
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 22,
    &quot;label&quot;: &quot;Name&quot;,
    &quot;right&quot;: &quot;â&quot;
   },
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 22,
    &quot;label&quot;: &quot;Health&quot;,
    &quot;right&quot;: &quot;â&quot;
   },
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 22,
    &quot;label&quot;: &quot;Distance&quot;,
    &quot;right&quot;: &quot;â&quot;
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Teleport to&quot;,
      &quot;icon&quot;: &quot;pointer&quot;,
      &quot;style&quot;: &quot;accent&quot;
     },
     {
      &quot;label&quot;: &quot;Pull here&quot;,
      &quot;icon&quot;: &quot;bolt&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Give all weapons&quot;,
    &quot;icon&quot;: &quot;fire&quot;,
    &quot;style&quot;: &quot;&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Knock him down&quot;,
    &quot;desc&quot;: &quot;æç»­å»å&quot;,
    &quot;on&quot;: false
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Kill aura&quot;,
    &quot;icon&quot;: &quot;skull&quot;
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Scatter radius&quot;,
    &quot;min&quot;: 1,
    &quot;max&quot;: 12,
    &quot;step&quot;: 0.5,
    &quot;fmt&quot;: &quot;%.1f m&quot;,
    &quot;value&quot;: 3
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Kill aura&quot;,
    &quot;desc&quot;: &quot;ææ®åç¯&quot;,
    &quot;on&quot;: false
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Spectate&quot;,
    &quot;icon&quot;: &quot;eye&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Observe player&quot;,
    &quot;desc&quot;: &quot;è§å¯ç©å®¶&quot;,
    &quot;on&quot;: false
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Kick&quot;,
    &quot;icon&quot;: &quot;skull&quot;
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Kick (host)&quot;,
    &quot;icon&quot;: &quot;trash&quot;,
    &quot;style&quot;: &quot;&quot;
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Kick (BE)&quot;,
    &quot;icon&quot;: &quot;skull&quot;,
    &quot;style&quot;: &quot;accent&quot;
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Kick (script host)&quot;,
    &quot;icon&quot;: &quot;warn&quot;,
    &quot;style&quot;: &quot;&quot;
   }
  ]
 },
 {
  &quot;name&quot;: &quot;Watch Dogs&quot;,
  &quot;title&quot;: &quot;Watch Dogs&quot;,
  &quot;desc&quot;: &quot;&quot;,
  &quot;icon&quot;: &quot;eye&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Scanner&quot;,
    &quot;icon&quot;: &quot;eye&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Hack lock&quot;,
    &quot;desc&quot;: &quot;Locks the ped, player or vehicle nearest the centre of your screen that you can actually see.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 1
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Scan range&quot;,
    &quot;min&quot;: 5,
    &quot;max&quot;: 150,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0f m&quot;,
    &quot;value&quot;: 45,
    &quot;gid&quot;: 2
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Aim box&quot;,
    &quot;min&quot;: 3,
    &quot;max&quot;: 60,
    &quot;step&quot;: 1,
    &quot;fmt&quot;: &quot;%.0f%&quot;,
    &quot;value&quot;: 22,
    &quot;gid&quot;: 3
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Profile overlay&quot;,
    &quot;desc&quot;: &quot;Draws the lock bracket and a small profile next to the target.&quot;,
    &quot;on&quot;: true,
    &quot;gid&quot;: 4
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Follow target&quot;,
    &quot;desc&quot;: &quot;Box sticks to the target instead of the crosshair. Only turn it on if the box lands on target.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 5
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Guide line&quot;,
    &quot;desc&quot;: &quot;Draws a 3D line from you to the locked target, so you always see exactly who it is.&quot;,
    &quot;on&quot;: true,
    &quot;gid&quot;: 6
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;HUD opacity&quot;,
    &quot;min&quot;: 0,
    &quot;max&quot;: 100,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0f%&quot;,
    &quot;value&quot;: 30,
    &quot;gid&quot;: 7
   },
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 24,
    &quot;label&quot;: &quot;&quot;,
    &quot;right&quot;: &quot;å¨è½¦ä¸&quot;
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;City&quot;,
    &quot;icon&quot;: &quot;globe&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Blackout&quot;,
    &quot;desc&quot;: &quot;Cuts the city lights around you.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 11
   }
  ]
 },
 {
  &quot;name&quot;: &quot;Toys&quot;,
  &quot;title&quot;: &quot;Toys&quot;,
  &quot;desc&quot;: &quot;Toys: physics and chaos â slow motion, ragdoll and wave buttons, traffic density, icy roads, car tricks and horn blasts.&quot;,
  &quot;icon&quot;: &quot;rocket&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Physics&quot;,
    &quot;icon&quot;: &quot;bolt&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Slow motion&quot;,
    &quot;desc&quot;: &quot;Slows the whole world down, you included.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 1
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Time scale&quot;,
    &quot;min&quot;: 0.1,
    &quot;max&quot;: 1,
    &quot;step&quot;: 0.05,
    &quot;fmt&quot;: &quot;%.2fx&quot;,
    &quot;value&quot;: 0.5,
    &quot;gid&quot;: 2
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Aim slow-mo&quot;,
    &quot;desc&quot;: &quot;Time crawls while you hold the aim button.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 3
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Chaos&quot;,
    &quot;icon&quot;: &quot;fire&quot;
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Wave radius&quot;,
    &quot;min&quot;: 5,
    &quot;max&quot;: 80,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0f m&quot;,
    &quot;value&quot;: 25,
    &quot;gid&quot;: 4
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Ragdoll wave&quot;,
      &quot;icon&quot;: &quot;bolt&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Panic wave&quot;,
      &quot;icon&quot;: &quot;users&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Earthquake&quot;,
      &quot;icon&quot;: &quot;fire&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Ped launch&quot;,
      &quot;icon&quot;: &quot;rocket&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Dress-up wave&quot;,
    &quot;desc&quot;: &quot;éè¿çäººä¸åæ¢è¡£æã&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 7
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Force push&quot;,
      &quot;icon&quot;: &quot;users&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Launch cars&quot;,
      &quot;icon&quot;: &quot;car&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;NPCs surrender&quot;,
    &quot;icon&quot;: &quot;users&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 9
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Riot&quot;,
    &quot;desc&quot;: &quot;éè¿çäººé½æ¿æªå²ä½ æ¥ã&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 10
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Play dead&quot;,
    &quot;desc&quot;: &quot;ææ­»äºåï¼&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 11
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Freeze wave&quot;,
    &quot;desc&quot;: &quot;éè¿çäººåè½¦å¨å»ä½ï¼å³æå°±æ¾å¼ã&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 12
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;See-through world&quot;,
    &quot;desc&quot;: &quot;WOW&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 13
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Restore model size&quot;,
    &quot;icon&quot;: &quot;wrench&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 14
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Big star&quot;,
    &quot;desc&quot;: &quot;éè¿çäººä¸¾çç¸æºå¯¹çä½ æç§ã&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 15
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Street brawl&quot;,
    &quot;desc&quot;: &quot;éè¿çäººäºç¸æèµ·æ¥ã&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 16
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Drunk camera&quot;,
    &quot;desc&quot;: &quot;The camera sways like you drank too much.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 17
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Stop shaking&quot;,
    &quot;icon&quot;: &quot;check&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 18
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Vortex&quot;,
    &quot;desc&quot;: &quot;Spins everything around you like a whirlwind.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 19
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Rainbow traffic&quot;,
    &quot;desc&quot;: &quot;Repaints every car around you with random colours.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 20
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Super jump&quot;,
    &quot;desc&quot;: &quot;Jump much higher while on foot.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 21
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Mounts&quot;,
    &quot;icon&quot;: &quot;users&quot;
   },
   {
    &quot;t&quot;: &quot;combo&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;Animal&quot;,
    &quot;items&quot;: [
     &quot;Cow&quot;,
     &quot;Deer&quot;,
     &quot;Mountain Lion&quot;,
     &quot;Boar&quot;,
     &quot;Pig&quot;,
     &quot;Coyote&quot;,
     &quot;Husky&quot;,
     &quot;Rottweiler&quot;,
     &quot;Golden Retriever&quot;,
     &quot;Pug&quot;
    ],
    &quot;idx&quot;: 0,
    &quot;gid&quot;: 22
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Ride animal&quot;,
      &quot;icon&quot;: &quot;plus&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Dismount&quot;,
      &quot;icon&quot;: &quot;check&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Seat height&quot;,
    &quot;min&quot;: -1,
    &quot;max&quot;: 2,
    &quot;step&quot;: 0.05,
    &quot;fmt&quot;: &quot;%.2f&quot;,
    &quot;value&quot;: -1,
    &quot;gid&quot;: 24
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Seat forward&quot;,
    &quot;min&quot;: -1.5,
    &quot;max&quot;: 1.5,
    &quot;step&quot;: 0.05,
    &quot;fmt&quot;: &quot;%.2f&quot;,
    &quot;value&quot;: -1.5,
    &quot;gid&quot;: 25
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Seat side&quot;,
    &quot;min&quot;: -1.5,
    &quot;max&quot;: 1.5,
    &quot;step&quot;: 0.05,
    &quot;fmt&quot;: &quot;%.2f&quot;,
    &quot;value&quot;: -1.5,
    &quot;gid&quot;: 26
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Tilt X&quot;,
    &quot;min&quot;: -180,
    &quot;max&quot;: 180,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0fÂ°&quot;,
    &quot;value&quot;: -180,
    &quot;gid&quot;: 27
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Tilt Y&quot;,
    &quot;min&quot;: -180,
    &quot;max&quot;: 180,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0fÂ°&quot;,
    &quot;value&quot;: -180,
    &quot;gid&quot;: 28
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Tilt Z&quot;,
    &quot;min&quot;: -180,
    &quot;max&quot;: 180,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0fÂ°&quot;,
    &quot;value&quot;: -180,
    &quot;gid&quot;: 29
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Convoy&quot;,
    &quot;icon&quot;: &quot;shield&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Convoy escort&quot;,
    &quot;desc&quot;: &quot;è½¦éæ¤é&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 30
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Bodyguards invincible&quot;,
    &quot;desc&quot;: &quot;ä¿éæ æ&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 31
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Convoy vehicles invincible&quot;,
    &quot;desc&quot;: &quot;ä¿éè½½å·æ æ&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 32
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Convoy rainbow paint&quot;,
    &quot;desc&quot;: &quot;ä¿éå½©è¹è½½å·&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 33
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Convoy shot damage&quot;,
    &quot;min&quot;: 1,
    &quot;max&quot;: 500,
    &quot;step&quot;: 1,
    &quot;fmt&quot;: &quot;%d&quot;,
    &quot;value&quot;: 60,
    &quot;gid&quot;: 34
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Street&quot;,
    &quot;icon&quot;: &quot;globe&quot;
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Traffic density&quot;,
    &quot;min&quot;: 0,
    &quot;max&quot;: 3,
    &quot;step&quot;: 0.5,
    &quot;fmt&quot;: &quot;%.1fx&quot;,
    &quot;value&quot;: 1,
    &quot;gid&quot;: 36
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Police ignore me&quot;,
    &quot;desc&quot;: &quot;Cops stop chasing you and forget your wanted level.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 37
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Icy roads&quot;,
    &quot;desc&quot;: &quot;Nearby vehicles slide around as if they were on ice.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 38
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Weather roulette&quot;,
    &quot;desc&quot;: &quot;Weather flips to a random type every couple of seconds.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 39
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Car magnet&quot;,
    &quot;desc&quot;: &quot;Drags every car around you towards you.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 40
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Magnet range&quot;,
    &quot;min&quot;: 10,
    &quot;max&quot;: 120,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0f m&quot;,
    &quot;value&quot;: 40,
    &quot;gid&quot;: 41
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Vehicle&quot;,
    &quot;icon&quot;: &quot;car&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Hop on space&quot;,
    &quot;desc&quot;: &quot;Press space while driving to jump.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 42
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Auto repair&quot;,
    &quot;desc&quot;: &quot;Your ride repairs itself while you drive.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 43
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Horn blast&quot;,
    &quot;desc&quot;: &quot;Honk to blast everything around your car away.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 44
   }
  ]
 },
 {
  &quot;name&quot;: &quot;Settings&quot;,
  &quot;title&quot;: &quot;Settings&quot;,
  &quot;desc&quot;: &quot;Settings: scale, language, menu key, config file and about. Tip: every change is saved automatically.&quot;,
  &quot;icon&quot;: &quot;cog&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Interface&quot;,
    &quot;icon&quot;: &quot;eye&quot;
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;UI scale&quot;,
    &quot;min&quot;: 80,
    &quot;max&quot;: 130,
    &quot;step&quot;: 1,
    &quot;fmt&quot;: &quot;%.0f%&quot;,
    &quot;value&quot;: 100,
    &quot;gid&quot;: 1
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Window opacity&quot;,
    &quot;min&quot;: 10,
    &quot;max&quot;: 100,
    &quot;step&quot;: 1,
    &quot;fmt&quot;: &quot;%.0f%&quot;,
    &quot;value&quot;: 75,
    &quot;gid&quot;: 2
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Toast notifications&quot;,
    &quot;desc&quot;: &quot;Animated toasts bottom right.&quot;,
    &quot;on&quot;: true,
    &quot;gid&quot;: 3
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Font Awesome icons&quot;,
    &quot;desc&quot;: &quot;Turn off if glyphs render as boxes.&quot;,
    &quot;on&quot;: true,
    &quot;gid&quot;: 4
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Debug overlay&quot;,
    &quot;desc&quot;: &quot;Shows a small status readout in the top-left corner.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 5
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Accent&quot;,
    &quot;icon&quot;: &quot;star&quot;
   },
   {
    &quot;t&quot;: &quot;combo&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;Colour&quot;,
    &quot;items&quot;: [
     &quot;Indigo&quot;,
     &quot;Cyan&quot;,
     &quot;Emerald&quot;,
     &quot;Amber&quot;,
     &quot;Rose&quot;
    ],
    &quot;idx&quot;: 0,
    &quot;gid&quot;: 6
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Rainbow accent&quot;,
    &quot;desc&quot;: &quot;The accent colour cycles through the rainbow. Tip: turn it off to go back to the colour picked above.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 7
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Background&quot;,
    &quot;icon&quot;: &quot;eye&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Background image&quot;,
    &quot;desc&quot;: &quot;Fills the menu with a picture from Reverie\\\\UI, stretched to fit.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 8
   },
   {
    &quot;t&quot;: &quot;combo&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;Image&quot;,
    &quot;items&quot;: [
     &quot;bg.png&quot;
    ],
    &quot;idx&quot;: 0,
    &quot;gid&quot;: 9
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 30,
    &quot;label&quot;: &quot;Refresh list&quot;,
    &quot;icon&quot;: &quot;bolt&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 10
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Background dim&quot;,
    &quot;min&quot;: 0,
    &quot;max&quot;: 90,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0f%&quot;,
    &quot;value&quot;: 45,
    &quot;gid&quot;: 11
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Language&quot;,
    &quot;icon&quot;: &quot;globe&quot;
   },
   {
    &quot;t&quot;: &quot;combo&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;Language&quot;,
    &quot;items&quot;: [
     &quot;English&quot;,
     &quot;ç®ä½ä¸­æ&quot;
    ],
    &quot;idx&quot;: 0,
    &quot;gid&quot;: 13
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Keys&quot;,
    &quot;icon&quot;: &quot;sliders&quot;
   },
   {
    &quot;t&quot;: &quot;keybind&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;Menu key&quot;,
    &quot;key&quot;: &quot;INSERT&quot;,
    &quot;gid&quot;: 14
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Config&quot;,
    &quot;icon&quot;: &quot;save&quot;
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 36,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Reset to defaults&quot;,
      &quot;icon&quot;: &quot;power&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Reset window&quot;,
      &quot;icon&quot;: &quot;power&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 36,
    &quot;label&quot;: &quot;Show path&quot;,
    &quot;icon&quot;: &quot;info&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 17
   }
  ]
 },
 {
  &quot;name&quot;: &quot;Tools&quot;,
  &quot;title&quot;: &quot;Tools&quot;,
  &quot;icon&quot;: &quot;pointer&quot;,
  &quot;desc&quot;: &quot;Tools: saved places, teleport presets and profiles. Tip: double-click a folder to expand, double-click a spot to teleport.&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Saved places&quot;,
    &quot;icon&quot;: &quot;pointer&quot;
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Save current place&quot;,
      &quot;icon&quot;: &quot;save&quot;,
      &quot;style&quot;: &quot;accent&quot;
     },
     {
      &quot;label&quot;: &quot;Delete last place&quot;,
      &quot;icon&quot;: &quot;trash&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 24,
    &quot;label&quot;: &quot;No saved places yet.&quot;
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Landmarks&quot;,
    &quot;icon&quot;: &quot;globe&quot;
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Airport&quot;,
      &quot;icon&quot;: &quot;pointer&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Mount Chiliad&quot;,
      &quot;icon&quot;: &quot;pointer&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Vinewood Sign&quot;,
      &quot;icon&quot;: &quot;pointer&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Del Perro Pier&quot;,
      &quot;icon&quot;: &quot;pointer&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Fort Zancudo&quot;,
      &quot;icon&quot;: &quot;pointer&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Sandy Shores&quot;,
      &quot;icon&quot;: &quot;pointer&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Profiles&quot;,
    &quot;icon&quot;: &quot;save&quot;
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Save profile&quot;,
      &quot;icon&quot;: &quot;save&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Load profile 1&quot;,
      &quot;icon&quot;: &quot;bolt&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Cooldowns&quot;,
    &quot;icon&quot;: &quot;bolt&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Remove Kosatka missile cooldown&quot;,
    &quot;desc&quot;: &quot;Removes the Kosatka submarine missile cooldown.&quot;,
    &quot;on&quot;: false
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Increase Kosatka missile range&quot;,
    &quot;desc&quot;: &quot;Raises Kosatka missile range to 99999.&quot;,
    &quot;on&quot;: false
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Remove appearance cooldown&quot;,
    &quot;desc&quot;: &quot;Removes the character appearance change cooldown.&quot;,
    &quot;on&quot;: false
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Free appearance change&quot;,
    &quot;desc&quot;: &quot;Makes appearance changes free.&quot;,
    &quot;on&quot;: false
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Remove CEO work cooldown&quot;,
    &quot;desc&quot;: &quot;Removes CEO work cooldowns.&quot;,
    &quot;on&quot;: false
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Remove client job cooldown&quot;,
    &quot;desc&quot;: &quot;Removes terrorbyte client job cooldowns.&quot;,
    &quot;on&quot;: false
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Remove payphone hit cooldown&quot;,
    &quot;icon&quot;: &quot;bolt&quot;,
    &quot;style&quot;: &quot;&quot;
   }
  ]
 },
 {
  &quot;name&quot;: &quot;Guard&quot;,
  &quot;title&quot;: &quot;Guard&quot;,
  &quot;desc&quot;: &quot;Guard: clears map spam and vision filters, and keeps an anti-crash camera ready.&quot;,
  &quot;icon&quot;: &quot;shield&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Filters&quot;,
    &quot;icon&quot;: &quot;eye&quot;
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Clear vision filter&quot;,
    &quot;icon&quot;: &quot;eye&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 1
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Keep clearing filters&quot;,
    &quot;desc&quot;: &quot;æç»­å é¤æ»¤é&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 2
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Clear camera distortion&quot;,
    &quot;icon&quot;: &quot;eye&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 3
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Keep clearing distortion&quot;,
    &quot;desc&quot;: &quot;æç»­æ¸çç¸å&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 4
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Notifications&quot;,
    &quot;icon&quot;: &quot;info&quot;
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Clear map notifications&quot;,
    &quot;icon&quot;: &quot;trash&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 5
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Only show tooltips&quot;,
    &quot;desc&quot;: &quot;Only show tooltip notifications; all other map notifications are hidden.&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 6
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Anti-crash&quot;,
    &quot;icon&quot;: &quot;bolt&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 50,
    &quot;label&quot;: &quot;Anti-crash camera&quot;,
    &quot;desc&quot;: &quot;é²å´©&quot;,
    &quot;on&quot;: false,
    &quot;gid&quot;: 7
   }
  ]
 },
 {
  &quot;name&quot;: &quot;Appearance&quot;,
  &quot;title&quot;: &quot;Appearance&quot;,
  &quot;desc&quot;: &quot;Appearance: HUD, watermark and notifications. Tip: adjust position and opacity here; the watermark can sit in any corner.&quot;,
  &quot;icon&quot;: &quot;eye&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;HUD&quot;,
    &quot;icon&quot;: &quot;eye&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Clock&quot;,
    &quot;desc&quot;: &quot;Shows the in-game clock on screen.&quot;,
    &quot;on&quot;: true,
    &quot;gid&quot;: 1
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Host info&quot;,
    &quot;desc&quot;: &quot;Shows the session host and how many players are online.&quot;,
    &quot;on&quot;: true,
    &quot;gid&quot;: 2
   },
   {
    &quot;t&quot;: &quot;combo&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;Watermark corner&quot;,
    &quot;items&quot;: [
     &quot;Top right&quot;,
     &quot;Top left&quot;,
     &quot;Bottom right&quot;,
     &quot;Bottom left&quot;
    ],
    &quot;idx&quot;: 0,
    &quot;gid&quot;: 3
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;Opacity&quot;,
    &quot;min&quot;: 0,
    &quot;max&quot;: 100,
    &quot;step&quot;: 5,
    &quot;fmt&quot;: &quot;%.0f%&quot;,
    &quot;value&quot;: 55,
    &quot;gid&quot;: 4
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Watermark&quot;,
    &quot;desc&quot;: &quot;Shows the menu name, version and hotkey on screen.&quot;,
    &quot;on&quot;: true,
    &quot;gid&quot;: 5
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Notifications&quot;,
    &quot;icon&quot;: &quot;info&quot;
   },
   {
    &quot;t&quot;: &quot;combo&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;Position&quot;,
    &quot;items&quot;: [
     &quot;Bottom right&quot;,
     &quot;Top right&quot;,
     &quot;Bottom left&quot;,
     &quot;Top left&quot;
    ],
    &quot;idx&quot;: 0,
    &quot;gid&quot;: 6
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 42,
    &quot;label&quot;: &quot;Max shown&quot;,
    &quot;min&quot;: 1,
    &quot;max&quot;: 8,
    &quot;step&quot;: 1,
    &quot;fmt&quot;: &quot;%.0f&quot;,
    &quot;value&quot;: 4,
    &quot;gid&quot;: 7
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Splash&quot;,
    &quot;icon&quot;: &quot;star&quot;
   },
   {
    &quot;t&quot;: &quot;toggle&quot;,
    &quot;h&quot;: 46,
    &quot;label&quot;: &quot;Splash&quot;,
    &quot;desc&quot;: &quot;Show a welcome card on load.&quot;,
    &quot;on&quot;: true,
    &quot;gid&quot;: 8
   },
   {
    &quot;t&quot;: &quot;slider&quot;,
    &quot;h&quot;: 44,
    &quot;label&quot;: &quot;Splash opacity&quot;,
    &quot;min&quot;: 0,
    &quot;max&quot;: 100,
    &quot;step&quot;: 2,
    &quot;fmt&quot;: &quot;%d%&quot;,
    &quot;value&quot;: 78,
    &quot;gid&quot;: 9
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Test splash&quot;,
    &quot;icon&quot;: &quot;star&quot;,
    &quot;style&quot;: &quot;&quot;,
    &quot;gid&quot;: 10
   }
  ]
 },
 {
  &quot;name&quot;: &quot;Heist&quot;,
  &quot;title&quot;: &quot;Heist&quot;,
  &quot;icon&quot;: &quot;skull&quot;,
  &quot;desc&quot;: &quot;Heist: cuts and one-click helpers for Cayo, Casino, Doomsday, Kortz and Apartment. Tip: pick a heist, set the cuts, press Apply, then use the prep buttons below.&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Payout&quot;,
    &quot;icon&quot;: &quot;skull&quot;
   },
   {
    &quot;t&quot;: &quot;tabbar&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Cayo&quot;,
      &quot;icon&quot;: &quot;car&quot;
     },
     {
      &quot;label&quot;: &quot;Casino&quot;,
      &quot;icon&quot;: &quot;skull&quot;
     },
     {
      &quot;label&quot;: &quot;Doomsday&quot;,
      &quot;icon&quot;: &quot;warn&quot;
     },
     {
      &quot;label&quot;: &quot;Kortz&quot;,
      &quot;icon&quot;: &quot;bolt&quot;
     },
     {
      &quot;label&quot;: &quot;Apartment&quot;,
      &quot;icon&quot;: &quot;save&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;tabpage&quot;,
    &quot;idx&quot;: 0,
    &quot;rows&quot;: [
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Cut slot 1 (host)&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 2000,
      &quot;step&quot;: 10,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 138
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Cut slot 2&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 2000,
      &quot;step&quot;: 10,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 138
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Cut slot 3&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 2000,
      &quot;step&quot;: 10,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 138
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Cut slot 4&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 2000,
      &quot;step&quot;: 10,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 138
     },
     {
      &quot;t&quot;: &quot;button&quot;,
      &quot;h&quot;: 34,
      &quot;label&quot;: &quot;Apply cuts&quot;,
      &quot;icon&quot;: &quot;check&quot;
     },
     {
      &quot;t&quot;: &quot;section&quot;,
      &quot;label&quot;: &quot;Cayo detector&quot;,
      &quot;icon&quot;: &quot;eye&quot;
     },
     {
      &quot;t&quot;: &quot;button&quot;,
      &quot;h&quot;: 34,
      &quot;label&quot;: &quot;Read Cayo stats&quot;,
      &quot;icon&quot;: &quot;info&quot;,
      &quot;style&quot;: &quot;accent&quot;
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Tequila value&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 100,
      &quot;step&quot;: 1,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 0
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Pearl necklace value&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 100,
      &quot;step&quot;: 1,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 0
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Bearer bonds value&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 100,
      &quot;step&quot;: 1,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 0
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Pink diamond value&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 100,
      &quot;step&quot;: 1,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 0
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Madrazo files value&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 100,
      &quot;step&quot;: 1,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 0
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Panther statue value&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 100,
      &quot;step&quot;: 1,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 0
     },
     {
      &quot;t&quot;: &quot;button&quot;,
      &quot;h&quot;: 34,
      &quot;label&quot;: &quot;Write target stats&quot;,
      &quot;icon&quot;: &quot;save&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;tabpage&quot;,
    &quot;idx&quot;: 1,
    &quot;rows&quot;: [
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Cut slot 1&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 300,
      &quot;step&quot;: 5,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 250
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Cut slot 2&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 300,
      &quot;step&quot;: 5,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 250
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Cut slot 3&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 300,
      &quot;step&quot;: 5,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 250
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Cut slot 4&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 300,
      &quot;step&quot;: 5,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 250
     },
     {
      &quot;t&quot;: &quot;button&quot;,
      &quot;h&quot;: 34,
      &quot;label&quot;: &quot;Apply casino cuts&quot;,
      &quot;icon&quot;: &quot;check&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;tabpage&quot;,
    &quot;idx&quot;: 2,
    &quot;rows&quot;: [
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Cut slot 1&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 400,
      &quot;step&quot;: 10,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 154
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Cut slot 2&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 400,
      &quot;step&quot;: 10,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 154
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Cut slot 3&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 400,
      &quot;step&quot;: 10,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 154
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Cut slot 4&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 400,
      &quot;step&quot;: 10,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 154
     },
     {
      &quot;t&quot;: &quot;button&quot;,
      &quot;h&quot;: 34,
      &quot;label&quot;: &quot;Apply doomsday cuts&quot;,
      &quot;icon&quot;: &quot;check&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;tabpage&quot;,
    &quot;idx&quot;: 3,
    &quot;rows&quot;: [
     {
      &quot;t&quot;: &quot;section&quot;,
      &quot;label&quot;: &quot;Kortz Center&quot;,
      &quot;icon&quot;: &quot;skull&quot;
     },
     {
      &quot;t&quot;: &quot;combo&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Primary target&quot;,
      &quot;items&quot;: [
       &quot;æåçæ¾çºµ&quot;,
       &quot;åä¸ªæ¸é&quot;,
       &quot;ç½é©¬çè¡°è½&quot;,
       &quot;åå¼&quot;,
       &quot;ç¾æä¸ç&quot;,
       &quot;åä¸ºä¹æ&quot;,
       &quot;çç±&quot;,
       &quot;çªæ¯&quot;,
       &quot;åº·ç¥æ²¡æ&quot;,
       &quot;æ´æ´çè³&quot;,
       &quot;åéå°å°&quot;,
       &quot;æ´çç é¡¹é¾çå¥³å­©&quot;,
       &quot;çç°åµä¸&quot;,
       &quot;åç&quot;,
       &quot;å¼å&quot;,
       &quot;æ½ç²¾ç æ&quot;,
       &quot;æ°´æ&quot;,
       &quot;æ¬²æ¬²ä¸ä¸&quot;,
       &quot;åå°èªç¶æ&quot;,
       &quot;æ¦¨å¹²&quot;,
       &quot;è¿èå®¶é&quot;,
       &quot;èè ç¬&quot;,
       &quot;ä¿¡ä»»&quot;,
       &quot;è³æ­»ä¸æ¸&quot;,
       &quot;é¡¶çç&quot;,
       &quot;å·§åè±ªå¤º&quot;,
       &quot;ç­åµç¸è§&quot;
      ],
      &quot;idx&quot;: 8
     },
     {
      &quot;t&quot;: &quot;combo&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Difficulty&quot;,
      &quot;items&quot;: [
       &quot;æ®éæ¨¡å¼&quot;,
       &quot;å°é¾æ¨¡å¼&quot;
      ],
      &quot;idx&quot;: 0
     },
     {
      &quot;t&quot;: &quot;combo&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Entry&quot;,
      &quot;items&quot;: [
       &quot;åå·¥å¥å£&quot;,
       &quot;å¤©çª&quot;,
       &quot;å¸è´§åº&quot;,
       &quot;ä¸æ°´é&quot;
      ],
      &quot;idx&quot;: 0
     },
     {
      &quot;t&quot;: &quot;combo&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Loadout&quot;,
      &quot;items&quot;: [
       &quot;è¡å¤´è£å¤&quot;,
       &quot;ä¿å®è£å¤&quot;,
       &quot;åç¨è£å¤&quot;
      ],
      &quot;idx&quot;: 0
     },
     {
      &quot;t&quot;: &quot;combo&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Getaway&quot;,
      &quot;items&quot;: [
       &quot;è£ç²å¡æå¡æ&quot;,
       &quot;æ­¼ç­èéå½¢ç&quot;,
       &quot;æ¼åå¹&quot;
      ],
      &quot;idx&quot;: 0
     },
     {
      &quot;t&quot;: &quot;combo&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Manchez color&quot;,
      &quot;items&quot;: [
       &quot;çº¢è²&quot;,
       &quot;èè²&quot;,
       &quot;ç»¿è²&quot;,
       &quot;é»è²&quot;
      ],
      &quot;idx&quot;: 0
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Guard routes&quot;,
      &quot;desc&quot;: &quot;Kortz prep: guard routes.&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Glass cutter&quot;,
      &quot;desc&quot;: &quot;Kortz prep: glass cutter.&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Power drills&quot;,
      &quot;desc&quot;: &quot;Kortz prep: power drills.&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;EMP device&quot;,
      &quot;desc&quot;: &quot;Kortz prep: EMP device.&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Weak guards&quot;,
      &quot;desc&quot;: &quot;Weaken guards in the finale.&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Scope secondary&quot;,
      &quot;desc&quot;: &quot;Mark all secondary targets as scoped.&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Scope POIs&quot;,
      &quot;desc&quot;: &quot;Mark all POIs as scouted.&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;buttons&quot;,
      &quot;h&quot;: 34,
      &quot;items&quot;: [
       {
        &quot;label&quot;: &quot;Apply Kortz setup&quot;,
        &quot;icon&quot;: &quot;check&quot;,
        &quot;style&quot;: &quot;accent&quot;
       },
       {
        &quot;label&quot;: &quot;Refresh board&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       }
      ]
     },
     {
      &quot;t&quot;: &quot;button&quot;,
      &quot;h&quot;: 34,
      &quot;label&quot;: &quot;Reset Kortz&quot;,
      &quot;icon&quot;: &quot;trash&quot;
     },
     {
      &quot;t&quot;: &quot;buttons&quot;,
      &quot;h&quot;: 34,
      &quot;items&quot;: [
       {
        &quot;label&quot;: &quot;Infinite lives&quot;,
        &quot;icon&quot;: &quot;heart&quot;
       },
       {
        &quot;label&quot;: &quot;Skip vault gate&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       }
      ]
     },
     {
      &quot;t&quot;: &quot;buttons&quot;,
      &quot;h&quot;: 34,
      &quot;items&quot;: [
       {
        &quot;label&quot;: &quot;Skip data hack&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       },
       {
        &quot;label&quot;: &quot;Skip fingerprint&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       }
      ]
     },
     {
      &quot;t&quot;: &quot;buttons&quot;,
      &quot;h&quot;: 34,
      &quot;items&quot;: [
       {
        &quot;label&quot;: &quot;Remove laser grid&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       },
       {
        &quot;label&quot;: &quot;Cut glass 100%&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       }
      ]
     },
     {
      &quot;t&quot;: &quot;buttons&quot;,
      &quot;h&quot;: 34,
      &quot;items&quot;: [
       {
        &quot;label&quot;: &quot;Accelerate primary&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       },
       {
        &quot;label&quot;: &quot;Accelerate secondary&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       }
      ]
     },
     {
      &quot;t&quot;: &quot;buttons&quot;,
      &quot;h&quot;: 34,
      &quot;items&quot;: [
       {
        &quot;label&quot;: &quot;Infinite bag&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       },
       {
        &quot;label&quot;: &quot;Unlock gallery&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       }
      ]
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 44,
      &quot;label&quot;: &quot;Secondary income&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 2000000,
      &quot;step&quot;: 1000,
      &quot;fmt&quot;: &quot;%.0f&quot;,
      &quot;value&quot;: 1000000
     },
     {
      &quot;t&quot;: &quot;button&quot;,
      &quot;h&quot;: 34,
      &quot;label&quot;: &quot;Set secondary income&quot;,
      &quot;icon&quot;: &quot;check&quot;
     },
     {
      &quot;t&quot;: &quot;combo&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Teleport&quot;,
      &quot;items&quot;: [
       &quot;éå¥æ¼å«å¢&quot;,
       &quot;éç¦å±±å«å¢&quot;,
       &quot;å¥½éº¦åå«å¢&quot;,
       &quot;åå·¥å¥å£&quot;,
       &quot;å¤©çª&quot;,
       &quot;ä¸æ°´é&quot;,
       &quot;å¸è´§åº&quot;,
       &quot;çµæ¢¯å£&quot;,
       &quot;æ¥¼æ¢¯å£&quot;,
       &quot;å±è§å®¤ä¸å±&quot;,
       &quot;å±è§å®¤äºæ¥¼&quot;,
       &quot;ç»å»&quot;,
       &quot;å°ä¸å®¤&quot;,
       &quot;çµèå¤&quot;
      ],
      &quot;idx&quot;: 0
     },
     {
      &quot;t&quot;: &quot;button&quot;,
      &quot;h&quot;: 34,
      &quot;label&quot;: &quot;Teleport&quot;,
      &quot;icon&quot;: &quot;pointer&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;tabpage&quot;,
    &quot;idx&quot;: 4,
    &quot;rows&quot;: [
     {
      &quot;t&quot;: &quot;section&quot;,
      &quot;label&quot;: &quot;Apartment heist&quot;,
      &quot;icon&quot;: &quot;save&quot;
     },
     {
      &quot;t&quot;: &quot;combo&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Apartment heist&quot;,
      &quot;items&quot;: [
       &quot;å¨ç¦é¶è¡&quot;,
       &quot;è¶ç±&quot;,
       &quot;çªè¢­äººéç ç©¶å®éªå®¤&quot;,
       &quot;é¦è½®åèµ&quot;,
       &quot;å¤ªå¹³æ´æ åé¶è¡&quot;
      ],
      &quot;idx&quot;: 0
     },
     {
      &quot;t&quot;: &quot;buttons&quot;,
      &quot;h&quot;: 34,
      &quot;items&quot;: [
       {
        &quot;label&quot;: &quot;Apply finale&quot;,
        &quot;icon&quot;: &quot;check&quot;,
        &quot;style&quot;: &quot;accent&quot;
       },
       {
        &quot;label&quot;: &quot;Force ready&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       }
      ]
     },
     {
      &quot;t&quot;: &quot;buttons&quot;,
      &quot;h&quot;: 34,
      &quot;items&quot;: [
       {
        &quot;label&quot;: &quot;Skip preps&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       },
       {
        &quot;label&quot;: &quot;Unlock board&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       }
      ]
     },
     {
      &quot;t&quot;: &quot;buttons&quot;,
      &quot;h&quot;: 34,
      &quot;items&quot;: [
       {
        &quot;label&quot;: &quot;Skip snake&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       },
       {
        &quot;label&quot;: &quot;Skip drill&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       }
      ]
     },
     {
      &quot;t&quot;: &quot;buttons&quot;,
      &quot;h&quot;: 34,
      &quot;items&quot;: [
       {
        &quot;label&quot;: &quot;Skip pacific hack&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       },
       {
        &quot;label&quot;: &quot;Infinite lives&quot;,
        &quot;icon&quot;: &quot;heart&quot;
       }
      ]
     },
     {
      &quot;t&quot;: &quot;buttons&quot;,
      &quot;h&quot;: 34,
      &quot;items&quot;: [
       {
        &quot;label&quot;: &quot;Quick finish&quot;,
        &quot;icon&quot;: &quot;bolt&quot;
       },
       {
        &quot;label&quot;: &quot;Criminal mastermind&quot;,
        &quot;icon&quot;: &quot;star&quot;
       }
      ]
     },
     {
      &quot;t&quot;: &quot;combo&quot;,
      &quot;h&quot;: 42,
      &quot;label&quot;: &quot;Teleport&quot;,
      &quot;items&quot;: [
       &quot;é¿å°å¡è¡&quot;,
       &quot;é¿å°å¡è¡è®¡åæ¿&quot;,
       &quot;æ­£ç´å°é&quot;,
       &quot;æ­£ç´å°éè®¡åæ¿&quot;,
       &quot;æ¥èå¤§å¦&quot;,
       &quot;æ¥èå¤§å¦è®¡åæ¿&quot;,
       &quot;ä½©ç½é«å°&quot;,
       &quot;ä½©ç½é«å°è®¡åæ¿&quot;,
       &quot;ä¸å¶æ &quot;,
       &quot;ä¸å¶æ è®¡åæ¿&quot;
      ],
      &quot;idx&quot;: 0
     },
     {
      &quot;t&quot;: &quot;button&quot;,
      &quot;h&quot;: 34,
      &quot;label&quot;: &quot;Teleport&quot;,
      &quot;icon&quot;: &quot;pointer&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;button&quot;,
    &quot;h&quot;: 34,
    &quot;label&quot;: &quot;Read current&quot;,
    &quot;icon&quot;: &quot;info&quot;
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;Auxiliary&quot;,
    &quot;icon&quot;: &quot;info&quot;
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 34,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Clear on-screen help&quot;,
      &quot;icon&quot;: &quot;trash&quot;
     },
     {
      &quot;label&quot;: &quot;Global XP = 1&quot;,
      &quot;icon&quot;: &quot;star&quot;
     }
    ]
   }
  ]
 },
 {
  &quot;name&quot;: &quot;ESP&quot;,
  &quot;title&quot;: &quot;ESP&quot;,
  &quot;icon&quot;: &quot;eye&quot;,
  &quot;desc&quot;: &quot;&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;two-col&quot;,
    &quot;left&quot;: [
     {
      &quot;t&quot;: &quot;section&quot;,
      &quot;label&quot;: &quot;ESP&quot;,
      &quot;icon&quot;: &quot;eye&quot;
     },
     {
      &quot;t&quot;: &quot;palette&quot;,
      &quot;h&quot;: 52,
      &quot;label&quot;: &quot;Snapline color&quot;,
      &quot;colors&quot;: [
       [
        255,
        92,
        92
       ],
       [
        255,
        168,
        64
       ],
       [
        250,
        226,
        72
       ],
       [
        118,
        240,
        110
       ],
       [
        92,
        232,
        220
       ],
       [
        96,
        172,
        255
       ],
       [
        176,
        132,
        255
       ],
       [
        255,
        120,
        214
       ],
       [
        240,
        240,
        245
       ],
       [
        152,
        158,
        176
       ],
       [
        44,
        48,
        58
       ],
       [
        132,
        255,
        160
       ]
      ],
      &quot;sel&quot;: 5
     },
     {
      &quot;t&quot;: &quot;palette&quot;,
      &quot;h&quot;: 52,
      &quot;label&quot;: &quot;Box color&quot;,
      &quot;colors&quot;: [
       [
        255,
        92,
        92
       ],
       [
        255,
        168,
        64
       ],
       [
        250,
        226,
        72
       ],
       [
        118,
        240,
        110
       ],
       [
        92,
        232,
        220
       ],
       [
        96,
        172,
        255
       ],
       [
        176,
        132,
        255
       ],
       [
        255,
        120,
        214
       ],
       [
        240,
        240,
        245
       ],
       [
        152,
        158,
        176
       ],
       [
        44,
        48,
        58
       ],
       [
        132,
        255,
        160
       ]
      ],
      &quot;sel&quot;: 4
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Enable ESP&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Snaplines&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Box&quot;,
      &quot;on&quot;: true
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Health bar&quot;,
      &quot;on&quot;: true
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Armor bar&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Weapon&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Name&quot;,
      &quot;on&quot;: true
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Wanted&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Level&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Distance&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Skip indoor&quot;,
      &quot;on&quot;: false
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 38,
      &quot;label&quot;: &quot;Text background&quot;,
      &quot;min&quot;: 0,
      &quot;max&quot;: 100,
      &quot;step&quot;: 5,
      &quot;fmt&quot;: &quot;%d%%&quot;,
      &quot;value&quot;: 55
     },
     {
      &quot;t&quot;: &quot;slider&quot;,
      &quot;h&quot;: 44,
      &quot;label&quot;: &quot;ESP range&quot;,
      &quot;min&quot;: 100,
      &quot;max&quot;: 500,
      &quot;step&quot;: 10,
      &quot;fmt&quot;: &quot;%dm&quot;,
      &quot;value&quot;: 300
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;No limit&quot;,
      &quot;on&quot;: false
     }
    ],
    &quot;right&quot;: [
     {
      &quot;t&quot;: &quot;section&quot;,
      &quot;label&quot;: &quot;Players&quot;,
      &quot;icon&quot;: &quot;users&quot;
     },
     {
      &quot;t&quot;: &quot;toggle&quot;,
      &quot;h&quot;: 46,
      &quot;label&quot;: &quot;Select all&quot;,
      &quot;on&quot;: true
     },
     {
      &quot;t&quot;: &quot;row&quot;,
      &quot;h&quot;: 30,
      &quot;label&quot;: &quot;DiamondDog&quot;,
      &quot;right&quot;: &quot;152m&quot;,
      &quot;icon&quot;: &quot;pointer&quot;
     },
     {
      &quot;t&quot;: &quot;row&quot;,
      &quot;h&quot;: 30,
      &quot;label&quot;: &quot;Mr_Fingers&quot;,
      &quot;right&quot;: &quot;88m&quot;,
      &quot;icon&quot;: &quot;check&quot;
     },
     {
      &quot;t&quot;: &quot;row&quot;,
      &quot;h&quot;: 30,
      &quot;label&quot;: &quot;Scooter&quot;,
      &quot;right&quot;: &quot;240m&quot;,
      &quot;icon&quot;: &quot;pointer&quot;
     },
     {
      &quot;t&quot;: &quot;row&quot;,
      &quot;h&quot;: 30,
      &quot;label&quot;: &quot;Kelvin&quot;,
      &quot;right&quot;: &quot;312m&quot;,
      &quot;icon&quot;: &quot;pointer&quot;
     }
    ]
   }
  ]
 },
 {
  &quot;name&quot;: &quot;Chat&quot;,
  &quot;title&quot;: &quot;Chatroom&quot;,
  &quot;icon&quot;: &quot;comment&quot;,
  &quot;desc&quot;: &quot;&quot;,
  &quot;rows&quot;: [
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 22,
    &quot;label&quot;: &quot;â connectingâ¦&quot;
   },
   {
    &quot;t&quot;: &quot;textbox&quot;,
    &quot;h&quot;: 30,
    &quot;label&quot;: &quot;Say&quot;,
    &quot;value&quot;: &quot;&quot;
   },
   {
    &quot;t&quot;: &quot;textbox&quot;,
    &quot;h&quot;: 30,
    &quot;label&quot;: &quot;Nick&quot;,
    &quot;value&quot;: &quot;&quot;
   },
   {
    &quot;t&quot;: &quot;info&quot;,
    &quot;h&quot;: 18,
    &quot;label&quot;: &quot;Nickname:&quot;
   },
   {
    &quot;t&quot;: &quot;buttons&quot;,
    &quot;h&quot;: 32,
    &quot;items&quot;: [
     {
      &quot;label&quot;: &quot;Send&quot;,
      &quot;icon&quot;: &quot;rocket&quot;,
      &quot;style&quot;: &quot;accent&quot;
     },
     {
      &quot;label&quot;: &quot;Paste&quot;,
      &quot;icon&quot;: &quot;save&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Reload&quot;,
      &quot;icon&quot;: &quot;bolt&quot;,
      &quot;style&quot;: &quot;&quot;
     },
     {
      &quot;label&quot;: &quot;Set nick&quot;,
      &quot;icon&quot;: &quot;user&quot;,
      &quot;style&quot;: &quot;&quot;
     }
    ]
   },
   {
    &quot;t&quot;: &quot;section&quot;,
    &quot;label&quot;: &quot;History Â· 3 messages&quot;,
    &quot;icon&quot;: &quot;clock&quot;
   },
   {
    &quot;t&quot;: &quot;chat&quot;,
    &quot;h&quot;: 21,
    &quot;time&quot;: &quot;21:04&quot;,
    &quot;nick&quot;: &quot;Reverie&quot;,
    &quot;text&quot;: &quot;everything for fun&quot;,
    &quot;mine&quot;: true
   },
   {
    &quot;t&quot;: &quot;chat&quot;,
    &quot;h&quot;: 21,
    &quot;time&quot;: &quot;21:05&quot;,
    &quot;nick&quot;: &quot;Shark&quot;,
    &quot;text&quot;: &quot;menu still open?&quot;,
    &quot;mine&quot;: false
   },
   {
    &quot;t&quot;: &quot;chat&quot;,
    &quot;h&quot;: 21,
    &quot;time&quot;: &quot;21:06&quot;,
    &quot;nick&quot;: &quot;Reverie&quot;,
    &quot;text&quot;: &quot;always&quot;,
    &quot;mine&quot;: true
   }
  ]
 }
];

&lt;/script&gt;
&lt;script&gt;
/* REVERIE UI Â· ä¸­æææ¡ï¼ä» Reverie/lang/zh-CN.lua æ½åï¼é®=çé¢è±æåæï¼å¼=ä¸­æï¼ */
window.REVERIE_ZH = {
 &quot;Home&quot;: &quot;ä¸»é¡µ&quot;,
 &quot;Self&quot;: &quot;ç©å®¶&quot;,
 &quot;Vehicle&quot;: &quot;è½½å·&quot;,
 &quot;World&quot;: &quot;ä¸ç&quot;,
 &quot;Players&quot;: &quot;ç©å®¶&quot;,
 &quot;Target&quot;: &quot;ç®æ &quot;,
 &quot;Settings&quot;: &quot;è®¾ç½®&quot;,
 &quot;Overview&quot;: &quot;æ¦è§&quot;,
 &quot;Tools&quot;: &quot;å·¥å·&quot;,
 &quot;Guard&quot;: &quot;é²æ¤&quot;,
 &quot;Appearance&quot;: &quot;å¤è§&quot;,
 &quot;Unlimited charge, unlimited thrust&quot;: &quot;æ éæ°ç¶ï¼æ éæ¨è¿&quot;,
 &quot;Full torque from a standstill: brutal acceleration and a much higher top speed.&quot;: &quot;èµ·æ­¥æ»¡æ­ç©ï¼å éæ´èºãæéææ»¡ã&quot;,
 &quot;Flips the vehicle back upright when it ends up on its roof. Tip: handy for stunt driving.&quot;: &quot;è½¦ç¿»è¿æ¥ï¼ä¾§ç¿»/åºæå¤©ï¼æ¶èªå¨æ¶æ­£ãæç¤ºï¼ç©ç¹ææ¶å¼çæ¹ä¾¿ã&quot;,
 &quot;Drives on water: the car floats on the surface instead of sinking. Tip: raise Float height if the car sits too low.&quot;: &quot;å¯ä»¥å¨æ°´é¢ä¸è¡é©¶ï¼è½¦æµ®å¨æ°´é¢ä¸ä¸å¾ä¸æ²ãæç¤ºï¼è½¦è´´æ°´å¤ªä½å°±è°å¤§ãæµ®æ°´é«åº¦ãã&quot;,
 &quot;Walk on water. Tip: keep it off when you want to swim down, it holds you on the surface.&quot;: &quot;å¯ä»¥å¨æ°´é¢ä¸èµ°ãæç¤ºï¼æ³æ½æ°´æ¶åå³æï¼å®ä¼ä¸ç´æä½ æå¨æ°´é¢ã&quot;,
 &quot;Fist of fire. Tip: hold RMB to charge, then LMB to punch out a flame; fists only, and no charge means no fire.&quot;: &quot;ç«ç°æ³ãæç¤ºï¼æä½å³é®èåï¼åç¨å·¦é®åºæ³å·ç«ï¼åªè½ç©ºæï¼ä¸èåä¸åºç«ã&quot;,
 &quot;Swords fly out from you to cut down nearby NPCs and empty vehicles. Tip: Sword count and Attack range below set how many and how far.&quot;: &quot;é£åä»ä½ èº«è¾¹é£åºï¼æ©æéè¿ç NPC åç©ºè½¦ãæç¤ºï¼ä¸é¢çãåæ°éãåãæ»å»èå´ãæ§å¶æ°éåè·ç¦»ã&quot;,
 &quot;Shoots wherever you look. Tip: fire with X only, and pick the version below (V3 is the railgun).&quot;: &quot;æä½ ççæ¹åå¼ç«ãæç¤ºï¼åªç¨ X å¼æªï¼ä¸é¢å¯éçæ¬ï¼V3 æ¯è½¨éç®ï¼ã&quot;,
 &quot;You take no damage at all. Tip: turn it off before using god-mode-sensitive features.&quot;: &quot;å®å¨ä¸åä¼¤å®³ãæç¤ºï¼éè¦è§è²æ­»äº¡çæµç¨åå³æã&quot;,
 &quot;No damage from bullets, fire, explosions, melee or drowning. Tip: turn it off when a mission needs you to die.&quot;: &quot;å­å¼¹ãç«ç°ãçç¸ãè¿æåæººæ°´é½ä¼¤ä¸å°ä½ ãæç¤ºï¼éè¦ä½ æ­»äº¡çæµç¨åå³æã&quot;,
 &quot;Overview: session status, quick toggles and shortcuts. Tip: every feature lives in the sidebar on the left.&quot;: &quot;æ»è§ï¼æå±ç¶æãå¿«æ·å¼å³åå¸¸ç¨å¥å£ãå·¦è¾¹æ ç®éå¨é½æï¼æ¢æ¢ç¿»ã&quot;,
 &quot;Self: health, invisibility, speed, fire fist, lightless shield, sword storm and spins. Tip: turn on Half god + Full health first, then pick what you need.&quot;: &quot;èªèº«ï¼è¡éãéèº«ãå éãç«æ³ãæ åæ¤ç¾ãä¸åå½å®åå°éèºãæç¤ºï¼åå¼ãåç¥ + å¨è¡ãä¿å½ï¼åæéå¼å¶ä»ã&quot;,
 &quot;Vehicle: top speed, water driving, rainbow paint and neon. Tip: get in the car first, then flip the switches.&quot;: &quot;è½½å·ï¼æéãæ°´ä¸è¡é©¶ãå½©è¹å·æ¼åéè¹ãæç¤ºï¼ååè¿è½¦éï¼åæå¼å¼å³ã&quot;,
 &quot;World: time of day and weather. Tip: pick a value, then press Apply (changing time online needs you to be host).&quot;: &quot;æ³è®©å¤©äº®å°±å¤©äº®ãæ³ä¸é¨å°±ä¸é¨ãéå¥½æ°å¼ç¹ãåºç¨ãï¼ä¸çå¬ä½ çã&quot;,
 &quot;Target: act on the player you picked in Lexis online players. Tip: select someone in Lexis first, then come back here.&quot;: &quot;æ¬é¡µä¸é¨å¯¹ä»ä½ å¨ Lexisãå¨çº¿ç©å®¶ãééä¸­çé£ä½ãåéäººï¼ååæ¥ã&quot;,
 &quot;Settings: scale, language, menu key, config file and about. Tip: every change is saved automatically.&quot;: &quot;ç¼©æ¾ãè¯­è¨ãå¼åºé®ãéç½®æä»¶åå³äºã&quot;,
 &quot;Tools: saved places, teleport presets and profiles. Tip: double-click a folder to expand, double-click a spot to teleport.&quot;: &quot;æ¶èåæ ãä¼ éé¢è®¾åå­æ¡£ãåå»å±å¼ï¼åå»å°ç¹ç´æ¥é£è¿å»ã&quot;,
 &quot;Guard: clears map spam and keeps an anti-crash camera ready.&quot;: &quot;æ¸æå°å¾å·å±éç¥ï¼é¡ºä¾¿å¤ä¸å°é²å´©éå¤´ã&quot;,
 &quot;Appearance: HUD, watermark and notifications. Tip: adjust position and opacity here; the watermark can sit in any corner.&quot;: &quot;HUDãæ°´å°åéç¥ãä½ç½®åéæåº¦éä½ è°ï¼æ°´å°ä¸¢åªä¸ªè§é½è¡ã&quot;,
 &quot;Heist: cuts and one-click helpers for Cayo, Casino, Doomsday, Kortz and Apartment. Tip: pick a heist, set the cuts, press Apply, then use the prep buttons below.&quot;: &quot;ä½©éç§å² / èµåº / æ«æ¥ / ç§å¹ / å¬å¯ï¼åçº¢åä¸é®åç½®ï¼é½å¨è¿å¿ã&quot;,
 &quot;Your character turns invisible to other players. Tip: switch it off in cutscenes or the camera may look odd.&quot;: &quot;è§è²å¯¹å«äººéèº«ãæç¤ºï¼è¿åºå¨ç»æ¶å»ºè®®å³æï¼å¦åéå¤´å¯è½æªæªçã&quot;,
 &quot;Health is refilled continuously. Tip: keep it on together with Half god.&quot;: &quot;è¡éæç»­åæ»¡ãæç¤ºï¼åãåæ æãä¸èµ·å¼æç¨³ã&quot;,
 &quot;You take almost no damage. Tip: heavy explosions can still hurt; use Lightless shield for those.&quot;: &quot;å ä¹ä¸åä¼¤å®³ãæç¤ºï¼å¤§çç¸ä»å¯è½ä¼¤å°ä½ ï¼é£ç§æåµç¨ãæ åæ¤ç¾ãã&quot;,
 &quot;Your weapons cycle through rainbow colours. Tip: works on ranged weapons you already own.&quot;: &quot;æ­¦å¨å¨å½©è¹è²ä¹é´å¾ªç¯ãæç¤ºï¼å¯¹ä½ å·²ææçæªæ¢°çæã&quot;,
 &quot;Anyone touching you is blown away by an invisible blast.&quot;: &quot;ç¢°ä½ çäººä¼è¢«æ å½¢çç¸è½°é£ã&quot;,
 &quot;Cutscenes are skipped automatically. Tip: keep it off in heists where a cutscene marks progress.&quot;: &quot;èªå¨è·³è¿è¿åºå¨ç»ãæç¤ºï¼æ¢å«éæäºè¿åºå¨ç»æ¯è¿åº¦èç¹ï¼å»ºè®®å³æã&quot;,
 &quot;Lifts your vehicle speed limit a lot. Tip: hold forward and avoid tight corners at full speed.&quot;: &quot;å¤§å¹æé«è½½å·éåº¦ä¸éãæç¤ºï¼å¨éæ¶å«æ¥ææ¹åã&quot;,
 &quot;Your vehicle rises when it goes under water. Tip: pair it with water driving so you can cross lakes.&quot;: &quot;è½½å·ä¸æ°´åä¼æµ®èµ·æ¥ãæç¤ºï¼åãæ°´ä¸è¡é©¶ãä¸èµ·ç¨å¯ä»¥æ¨ªç©¿æ¹æ³ã&quot;,
 &quot;Free flight. Tip: aim with the camera, WASD to fly, Space up and Ctrl down.&quot;: &quot;èªç±é£è¡ãæç¤ºï¼ç¨éå¤´çåï¼WASD é£ï¼ç©ºæ ¼ä¸åãCtrl ä¸éã&quot;,
 &quot;Paint fades through a rainbow. Tip: only the driver's view changes instantly; passengers see the current colour.&quot;: &quot;è½¦èº«æ¼é¢å½©è¹æ¸åãæç¤ºï¼åªæé©¾é©¶èè§è§é©¬ä¸åï¼ä¹å®¢çå°çæ¯å½åé¢è²ã&quot;,
 &quot;Neon fades through a rainbow. Tip: turn it off while you are only a passenger.&quot;: &quot;éè¹ç¯å½©è¹æ¸åãæç¤ºï¼åªå½ä¹å®¢æ¶æå®å³æã&quot;,
 &quot;Keeps the rainbow effects off while someone else drives. Tip: handy when riding with friends.&quot;: &quot;å«äººå¼è½¦æ¶èªå¨å³é­å½©è¹ææãæç¤ºï¼åæååè½¦æ¶ç¨ã&quot;,
 &quot;Kortz prep: guard routes.&quot;: &quot;ç§å¹åç½®ï¼å·¡é»è·¯çº¿ã&quot;,
 &quot;Kortz prep: glass cutter.&quot;: &quot;ç§å¹åç½®ï¼ç»çåå²å¨ã&quot;,
 &quot;Kortz prep: power drills.&quot;: &quot;ç§å¹åç½®ï¼çµé»ã&quot;,
 &quot;Kortz prep: EMP device.&quot;: &quot;ç§å¹åç½®ï¼çµç£èå²è£ç½®ã&quot;,
 &quot;Heist&quot;: &quot;æ¢å«&quot;,
 &quot;Watch Dogs&quot;: &quot;çé¨ç&quot;,
 &quot;Watch Dogs: point the crosshair at people and the scanner locks whoever sits closest to the centre of the screen, online players included. Tip: turn on Hack lock, aim at someone, then use the hack buttons below.&quot;: &quot;çé¨çï¼æåæå¯¹çäººï¼æ«æå¨ä¼éå®å±å¹ä¸æé è¿ä¸­å¿çé£ä¸ªäººï¼å¨çº¿ç©å®¶ä¹ç®ãæç¤ºï¼åå¼ãéªå¥éå®ãï¼å¯¹çç®æ ç«å¥½ï¼åç¨ä¸é¢çéªå¥æé®ã&quot;,
 &quot;Toys&quot;: &quot;ç©å·&quot;,
 &quot;Toys: physics and chaos â slow motion, ragdoll and wave buttons, traffic density, icy roads, car tricks and horn blasts.&quot;: &quot;ç©å·ï¼ç©çä¸æ··ä¹±ââæ¢å¨ä½ãæ¾åååç§æ³¢ãäº¤éå¯åº¦ãå°é¢ãè½½å·è±æ´»ååå­å²å»æ³¢ã&quot;,
 &quot;Self: health, invisibility, fire fist, sword storm, spins, clothing, coordinates, weapons and a forward blink.&quot;: &quot;èªæºï¼è¡éãéèº«ãç«æ³ãä¸åå½å®ãéèºãæè£ãåæ ãæ­¦å¨ãååç¬ç§»ã&quot;,
 &quot;Box sticks to the target instead of the crosshair. Only turn it on if the box lands on target.&quot;: &quot;éå®æ¡è´´å¨ç®æ èº«ä¸ï¼ä¸è·åæèµ°ãåªæéå®æ¡ç¡®å®è½å¨ç®æ ä¸æ¶æå»ºè®®å¼ã&quot;,
 &quot;Draws a 3D line from you to the locked target, so you always see exactly who it is.&quot;: &quot;ä»ä½ èº«ä¸ç»ä¸æ¡ 3D çº¿è¿å°è¢«éå®çç®æ ï¼ä¸ç¼çæ¸éçæ¯è°ã&quot;,
 &quot;Vehicle: top speed, water driving, god mode, ghost mode, rainbow paint, neon and a vehicle spawner with max upgrades.&quot;: &quot;è½½å·ï¼æéãæ°´ä¸è¡é©¶ãæ æãå¹½çµè½¦ãå½©è¹å·æ¼ãéè¹ï¼ä»¥åä¸é®å·æ»¡æ¹è½½å·ã&quot;,
 &quot;Guard: clears map spam and vision filters, and keeps an anti-crash camera ready.&quot;: &quot;é²æ¤ï¼æ¸æå°å¾å·å±éç¥åæ»¤éï¼å¹¶å¤ä¸å°é²å´©éå¤´ã&quot;,
 &quot;Toys: physics and chaos â low gravity, slow motion, ragdoll and panic waves, earthquakes, vehicle hops and auto repair. Tip: the wave radius slider drives every chaos button.&quot;: &quot;ç©å·ï¼ç©çåæ··ä¹±ââä½éåãæ¢å¨ä½ãæ¾åå¨åºãæç¾¤ãå°éãç©ºæ ¼è·³è½¦åèªå¨ä¿®è½¦ãæç¤ºï¼ãæ³¢å¨åå¾ãæ»æ¡å³å®æææ··ä¹±æé®çä½ç¨èå´ã&quot;,
 &quot;Vehicle: top speed, water driving, god mode, ghost mode, rainbow paint, neon, a vehicle spawner with max upgrades. Tip: get in the car first, then flip the switches.&quot;: &quot;æéãæ°´ä¸è·ãæ æãå¹½çµè½¦ãå½©è¹ãéè¹ãå·è½¦æ»¡æ¹ãååè¿è½¦éåæ¨å¼å³ã&quot;,
 &quot;Toys: physics and chaos â gravity, slow motion, aim slow-mo, ragdoll, panic, freeze, launch, riot, brawl and force waves, night and thermal vision, traffic density, icy roads, car magnet, vortex, weather roulette, super jump, vehicle hops, auto repair and horn blasts. Tip: the wave radius slider drives every chaos button.&quot;: &quot;ç©å·ï¼ç©çä¸æ··ä¹±ââéåãæ¢å¨ä½ãçåæ¢å¨ä½ãæ¾å/æç¾¤/å®èº«/éä¸å¤©/æ´å¨/ç«å¹¶/ååºæ³¢ãå¤è§åç­æåãäº¤éå¯åº¦ãå°é¢ãå¿µåå¸è½¦ãæ¼©æ¶¡ãå¤©æ°è½®çãè¶çº§è·³ãç©ºæ ¼è·³è½¦ãèªå¨ä¿®è½¦ååå­å²å»æ³¢ãæç¤ºï¼ãæ³¢å¨åå¾ãæ»æ¡å³å®æææ··ä¹±æé®çä½ç¨èå´ã&quot;,
 &quot;Self: health, invisibility, fire fist, sword storm, spins, clothing, coordinates, weapons and a forward blink. Tip: turn on Half god + Full health first, then pick what you need.&quot;: &quot;è¡éãéèº«ãç«æ³ãä¸åå½å®ãéèºãæè£ãåæ ãæ­¦å¨ãååç¬ç§»ãåå¼ãåç¥ + å¨è¡ãä¿å½ã&quot;,
 &quot;Vehicle: top speed, water driving, god mode, rainbow paint, neon and a vehicle spawner. Tip: get in the car first, then flip the switches.&quot;: &quot;æéãæ°´ä¸è·ãæ æãå½©è¹ãéè¹ãå·è½¦ãååè¿è½¦éåæ¨å¼å³ã&quot;,
 &quot;Watch Dogs: point the crosshair at people and the scanner locks whoever sits closest to the centre of the screen, online players included. Tip: turn on Hack lock, aim at someone, then use the hack buttons below. City has remote start, traffic jam and blackout.&quot;: &quot;çé¨çï¼æåæå¯¹çäººï¼æ«æå¨ä¼éå®å±å¹ä¸æé è¿ä¸­å¿çé£ä¸ªäººï¼å¨çº¿ç©å®¶ä¹ç®ãæç¤ºï¼åå¼ãéªå¥éå®ãï¼å¯¹çç®æ ç«å¥½ï¼åç¨ä¸é¢çéªå¥æé®ããåå¸ãéæè¿ç¨å¯å¨ãå¨åå µè½¦ååçµã&quot;,
 &quot;Local player â invincibility, health, wanted level, waypoint teleport.&quot;: &quot;æ¬å°ç©å®¶ï¼æ æãè¡éãéç¼ç­çº§ãä¼ éå°å¯¼èªç¹ã&quot;,
 &quot;ACCOUNT&quot;: &quot;è´¦æ·&quot;,
 &quot;click Â· drag header Â· wheel scroll&quot;: &quot;ç¹å» Â· æå¨æ é¢æ  Â· æ»è½®æ»å¨&quot;,
 &quot;Session&quot;: &quot;ä¼è¯&quot;,
 &quot;Quick actions&quot;: &quot;å¿«æ·æä½&quot;,
 &quot;Protection&quot;: &quot;é²æ¤&quot;,
 &quot;Health&quot;: &quot;çå½&quot;,
 &quot;Navigation&quot;: &quot;å¯¼èª&quot;,
 &quot;Player&quot;: &quot;ç©å®¶&quot;,
 &quot;Session id&quot;: &quot;ä¼è¯ ID&quot;,
 &quot;Rank&quot;: &quot;ç­çº§&quot;,
 &quot;Lexis notify&quot;: &quot;Lexis éç¥&quot;,
 &quot;Close UI&quot;: &quot;å³é­çé¢&quot;,
 &quot;Armour&quot;: &quot;æ¤ç²&quot;,
 &quot;Apply stats&quot;: &quot;åºç¨å±æ§&quot;,
 &quot;Clear wanted&quot;: &quot;æ¸é¤éç¼&quot;,
 &quot;No players synced yet.&quot;: &quot;è¿æ²¡åæ­¥å°ç©å®¶ã&quot;,
 &quot;Shows the session host and how many players are online.&quot;: &quot;æ¾ç¤ºæå±ä¸»æºåå¨çº¿äººæ°ã&quot;,
 &quot;Shows the menu name, version and hotkey on screen.&quot;: &quot;å¨å±å¹ä¸æ¾ç¤ºèååãçæ¬åå¼åºé®ã&quot;,
 &quot;hdr.sub&quot;: &quot;reverie v%s&quot;,
 &quot;sec.session_n&quot;: &quot;ä¼è¯ (%d)&quot;,
 &quot;home.players&quot;: &quot;%d åç©å®¶&quot;,
 &quot;Invisible&quot;: &quot;éèº«&quot;,
 &quot;Flight&quot;: &quot;é£è¡&quot;,
 &quot;Fly vehicle&quot;: &quot;è½½å·é£è¡&quot;,
 &quot;Fly speed&quot;: &quot;é£è¡éåº¦&quot;,
 &quot;Body follows the camera; WASD to move, Space/Ctrl up-down.&quot;: &quot;è½¦èº«è·éè§è§ï¼WASD ç§»å¨ï¼ç©ºæ ¼ä¸å / Ctrl ä¸éã&quot;,
 &quot;Rainbow&quot;: &quot;å½©è¹&quot;,
 &quot;Water walk&quot;: &quot;æ°´ä¸è¡èµ°&quot;,
 &quot;Bunny hop&quot;: &quot;åå­è·³&quot;,
 &quot;Hold Space to jump continuously; hold Shift too to build speed with each jump (up to 30x).&quot;: &quot;æä½ç©ºæ ¼è¿ç»­è·³è·ï¼åæ¶æä½ Shift ä¼éè·³è·æ¬¡æ°å éï¼æé« 30 åï¼ã&quot;,
 &quot;Laser eyes&quot;: &quot;æ¿åç¼&quot;,
 &quot;Spin&quot;: &quot;å°éèº&quot;,
 &quot;Big spin&quot;: &quot;å¤§éèº&quot;,
 &quot;Big spin 1.6&quot;: &quot;å¤§éèº1.6&quot;,
 &quot;Spin target&quot;: &quot;æ»å»ç®æ &quot;,
 &quot;Random yaw rotation while no WASD is held (old script _U_spin).&quot;: &quot;ä¸æ WASD æ¶éæºæ°´å¹³æè½¬ã&quot;,
 &quot;Random rotation on all three axes while no WASD is held (old script _U_spin_16).&quot;: &quot;ä¸æ WASD æ¶éæºä¸è½´æè½¬ã&quot;,
 &quot;NPCs&quot;: &quot;NPC&quot;,
 &quot;NPCs + players&quot;: &quot;NPC+ç©å®¶&quot;,
 &quot;None&quot;: &quot;æ &quot;,
 &quot;Attack range&quot;: &quot;æ»å»èå´&quot;,
 &quot;Lightless shield&quot;: &quot;æ åæ¤ç¾&quot;,
 &quot;Sword storm&quot;: &quot;ä¸åå½å®&quot;,
 &quot;Sword count&quot;: &quot;åæ°é&quot;,
 &quot;Sword damage&quot;: &quot;åä¼¤å®³&quot;,
 &quot;Sword rain&quot;: &quot;åé¨&quot;,
 &quot;Observe swords&quot;: &quot;è§å¯&quot;,
 &quot;Swords fall from the sky onto nearby targets.&quot;: &quot;åä»å¤©èéç ¸åéè¿ç®æ ã&quot;,
 &quot;Skip cutscene&quot;: &quot;è·³è¿è¿åº&quot;,
 &quot;Give weapon&quot;: &quot;è·åæ­¦å¨&quot;,
 &quot;Weapon&quot;: &quot;æ­¦å¨&quot;,
 &quot;Give weapon failed.&quot;: &quot;ç»æ­¦å¨å¤±è´¥ã&quot;,
 &quot;Mission&quot;: &quot;ä»»å¡&quot;,
 &quot;Fire fist&quot;: &quot;ç«ç°æ³&quot;,
 &quot;Karma&quot;: &quot;å ææ¥åº&quot;,
 &quot;Full health&quot;: &quot;è¡æ¡æ é&quot;,
 &quot;Half god&quot;: &quot;åæ æ&quot;,
 &quot;Invincible&quot;: &quot;æ æ&quot;,
 &quot;Clothing&quot;: &quot;æè£&quot;,
 &quot;Part&quot;: &quot;é¨ä½&quot;,
 &quot;Style&quot;: &quot;æ¬¾å¼&quot;,
 &quot;Texture&quot;: &quot;è´´å¾&quot;,
 &quot;Apply&quot;: &quot;åºç¨&quot;,
 &quot;Random&quot;: &quot;éæº&quot;,
 &quot;Coordinates&quot;: &quot;åæ &quot;,
 &quot;Teleport&quot;: &quot;ä¼ é&quot;,
 &quot;Read current&quot;: &quot;è¯»åå½åå¼&quot;,
 &quot;Weapons&quot;: &quot;æ­¦å¨&quot;,
 &quot;Give all&quot;: &quot;è·åå¨é¨æ­¦å¨&quot;,
 &quot;Infinite ammo&quot;: &quot;æ éå¤å¼¹&quot;,
 &quot;No reload&quot;: &quot;ä¸ç¨æ¢å¼¹&quot;,
 &quot;Damage&quot;: &quot;ä¼¤å®³åç&quot;,
 &quot;Blink forward&quot;: &quot;ååç¬ç§»&quot;,
 &quot;Save outfit&quot;: &quot;ä¿å­å¥è£&quot;,
 &quot;Wear outfit&quot;: &quot;ç©¿ä¸å¥è£&quot;,
 &quot;Spins everything around you like a whirlwind.&quot;: &quot;æå¨å´çäººåè½¦å·æä¸éµæé£ã&quot;,
 &quot;Unlock top speed&quot;: &quot;è§£éæé&quot;,
 &quot;XML vehicle&quot;: &quot;XML è½½å·&quot;,
 &quot;XML file&quot;: &quot;XML æä»¶&quot;,
 &quot;Custom XML path&quot;: &quot;èªå®ä¹ XML è·¯å¾&quot;,
 &quot;Spawn from XML&quot;: &quot;å·åº XML è½½å·&quot;,
 &quot;Spawned XML vehicles&quot;: &quot;å·²å·åºç XML è½½å·&quot;,
 &quot;No XML vehicle spawned yet&quot;: &quot;è¿æ²¡æå·è¿ XML è½½å·&quot;,
 &quot;Teleport it to me&quot;: &quot;ä¼ éå°æ&quot;,
 &quot;Teleport to it&quot;: &quot;ä¼ éå°å®&quot;,
 &quot;Get in driver seat&quot;: &quot;ä¼ éè¿é©¾é©¶å®¤&quot;,
 &quot;Delete&quot;: &quot;å é¤&quot;,
 &quot;Why didn't you tell me about such a fast car&quot;: &quot;æè¿ä¹å¿«çè½¦æä¹ä¸æ©ç¹åè¯æ&quot;,
 &quot;Why didn't you tell me about such a fast car sooner&quot;: &quot;æè¿ä¹å¿«çè½¦ä½ æä¹ä¸æ©ç¹åè¯æ&quot;,
 &quot;Roadster&quot;: &quot;Roadster&quot;,
 &quot;Instant torque&quot;: &quot;ç¬æ¶æ­ç©&quot;,
 &quot;SpaceX thrusters&quot;: &quot;SpaceX æ¨è¿å¨&quot;,
 &quot;Thrust power&quot;: &quot;æ¨è¿å&quot;,
 &quot;Unlimited thrusters&quot;: &quot;æ éæ°ç¶&quot;,
 &quot;Regen braking&quot;: &quot;å¨è½åæ¶&quot;,
 &quot;Grip&quot;: &quot;æå°å&quot;,
 &quot;Summon vehicle&quot;: &quot;å¬å¤è½½å·&quot;,
 &quot;Auto flip&quot;: &quot;èªå¨ç¿»è½¬&quot;,
 &quot;Water driving&quot;: &quot;æ°´ä¸è¡é©¶&quot;,
 &quot;Float height&quot;: &quot;æµ®æ°´é«åº¦&quot;,
 &quot;Rainbow paint&quot;: &quot;å½©è¹æ¶è£&quot;,
 &quot;Rainbow neon&quot;: &quot;å½©è¹éè¹ç¯&quot;,
 &quot;Disable as passenger&quot;: &quot;ä¹å®¢æ¶ç¦ç¨&quot;,
 &quot;Spawner&quot;: &quot;å·è½¦&quot;,
 &quot;Model&quot;: &quot;è½¦å&quot;,
 &quot;Spawn vehicle&quot;: &quot;å·åºè½½å·&quot;,
 &quot;Vehicle god mode&quot;: &quot;è½½å·æ æ&quot;,
 &quot;Your car cannot be wrecked by crashes or explosions.&quot;: &quot;è½¦æä¸åä¹ç¸ä¸åã&quot;,
 &quot;Custom&quot;: &quot;èªå®ä¹&quot;,
 &quot;Spawn custom&quot;: &quot;å·åºèªå®ä¹&quot;,
 &quot;Ghost car&quot;: &quot;å¹½çµè½¦&quot;,
 &quot;Your car passes straight through traffic and walls.&quot;: &quot;ä½ çè½¦è½ç©¿è¿å¶ä»è½¦åå¢ã&quot;,
 &quot;Max upgrades&quot;: &quot;æ»¡æ¹è½½å·&quot;,
 &quot;Enter on spawn&quot;: &quot;å·è½¦å³ä¸è½¦&quot;,
 &quot;Puts you straight into the car you spawn.&quot;: &quot;å·åºæ¥çè½¦ç´æ¥æä½ æ¾è¿é©¾é©¶ä½ã&quot;,
 &quot;Repair now&quot;: &quot;ç«å»ä¿®è½¦&quot;,
 &quot;#ArmedETR1&quot;: &quot;æ­¦è£ ETR1&quot;,
 &quot;aaaSHadowMechaV1&quot;: &quot;æå½±æºç² V1&quot;,
 &quot;aaaWarBaseVehical&quot;: &quot;æäºåºå°è½¦&quot;,
 &quot;Apoc Penetrator 1.5&quot;: &quot;æ«ä¸ç©¿éè 1.5&quot;,
 &quot;BIGHEAD AngryDog&quot;: &quot;æ¤æç¬&quot;,
 &quot;BIGHEAD ArmoredMechanic&quot;: &quot;è£ç²æºæ¢°å¸&quot;,
 &quot;BIGHEAD Body Collector&quot;: &quot;æ¶å°¸è½¦&quot;,
 &quot;BIGHEAD BurgerTruck&quot;: &quot;æ±å ¡å¡è½¦&quot;,
 &quot;BIGHEAD Cinema Car&quot;: &quot;çµå½±é¢è½¦&quot;,
 &quot;BIGHEAD CustomUFO2&quot;: &quot;å®å¶é£ç¢&quot;,
 &quot;BIGHEAD Dogsled2&quot;: &quot;çæéªæ©&quot;,
 &quot;BIGHEAD FutureBike2&quot;: &quot;æªæ¥æ©æ II&quot;,
 &quot;BIGHEAD FutureBike3&quot;: &quot;æªæ¥æ©æ III&quot;,
 &quot;BIGHEAD JuiceDump&quot;: &quot;ææ±ç¿»æè½¦&quot;,
 &quot;BIGHEAD LightBike&quot;: &quot;åè½®æ©æ&quot;,
 &quot;BIGHEAD LightIssi&quot;: &quot;åè½®è¿·ä½ &quot;,
 &quot;BIGHEAD MoneyMonster&quot;: &quot;éç¥¨æªå½&quot;,
 &quot;BIGHEAD MurderCar&quot;: &quot;å¶è½¦&quot;,
 &quot;BIGHEAD ParagonTruck&quot;: &quot;å¸èå¡è½¦&quot;,
 &quot;BIGHEAD PurpleGangGunner&quot;: &quot;ç´«è²å¸®æ´¾ç®æ&quot;,
 &quot;BIGHEAD RC Chop&quot;: &quot;é¥æ§æ©æ&quot;,
 &quot;BIGHEAD RC Ped&quot;: &quot;é¥æ§å°äºº&quot;,
 &quot;BIGHEAD RC Ramp&quot;: &quot;é¥æ§è·³å°&quot;,
 &quot;BIGHEAD SOLIDRAMP&quot;: &quot;å®å¿æå¡&quot;,
 &quot;BIGHEAD SOLIDSTUNTJUMP&quot;: &quot;å®å¿ç¹æè·³å°&quot;,
 &quot;BIGHEAD TrainBike&quot;: &quot;ç«è½¦æ©æ&quot;,
 &quot;BIGHEAD UFO&quot;: &quot;é£ç¢&quot;,
 &quot;BIGHEAD XMAS&quot;: &quot;å£è¯ç¹å«ç&quot;,
 &quot;Butcher Heli&quot;: &quot;å± å¤«ç´åæº&quot;,
 &quot;Cargo Ship (Tugboat)&quot;: &quot;è´§è½®ï¼æè¹ï¼&quot;,
 &quot;Hover Spaceship&quot;: &quot;æ¬æµ®é£è¹&quot;,
 &quot;Hoverbike&quot;: &quot;æ¬æµ®æ©æ&quot;,
 &quot;Katana-Mobile&quot;: &quot;åéæè½¦&quot;,
 &quot;NEON - Lowell&quot;: &quot;éè¹Â·æ´å¨å°&quot;,
 &quot;Neon - Osiris GT-500&quot;: &quot;éè¹Â·å¥¥è¥¿éæ¯ GT-500&quot;,
 &quot;NuclearRocket&quot;: &quot;æ ¸ç«ç®­&quot;,
 &quot;Old Tank&quot;: &quot;èå¼å¦å&quot;,
 &quot;Poolmobile (no peds)&quot;: &quot;æ³³æ± è½¦ï¼æ äººï¼&quot;,
 &quot;Realistic ghost rider motorbike&quot;: &quot;æ¶çµéªå£«æ©æ&quot;,
 &quot;RHINO TRON 2.0&quot;: &quot;ççæè½¦ 2.0&quot;,
 &quot;Robot&quot;: &quot;æºå¨äºº&quot;,
 &quot;ROBOT'1-SYXAPUK&quot;: &quot;æºå¨äºº I å&quot;,
 &quot;ROBOT'2-SYXAPUK&quot;: &quot;æºå¨äºº II å&quot;,
 &quot;ROBOT'3-SYXAPUK&quot;: &quot;æºå¨äºº III å&quot;,
 &quot;Robot'4-Syxapuk&quot;: &quot;æºå¨äºº IV å&quot;,
 &quot;Rocket Ramp&quot;: &quot;ç«ç®­è·³å°&quot;,
 &quot;Santa Car Xmas 2016 Edition&quot;: &quot;å£è¯èäººè½¦ 2016 ç&quot;,
 &quot;Spider&quot;: &quot;èè&quot;,
 &quot;Subway&quot;: &quot;å°éåè½¦&quot;,
 &quot;T20 Police&quot;: &quot;T20 è­¦è½¦&quot;,
 &quot;The Dreadnaught&quot;: &quot;æ çå·&quot;,
 &quot;TheFastFoliage&quot;: &quot;ç¾é£æ å¶è½¦&quot;,
 &quot;toutfeutoutflamme&quot;: &quot;çç«æè½¦&quot;,
 &quot;Truck With Ramp&quot;: &quot;å¸¦è·³å°å¡è½¦&quot;,
 &quot;Ultimate Dozer&quot;: &quot;ç»ææ¨åæº&quot;,
 &quot;ZapperTruck&quot;: &quot;çµå»å¡è½¦&quot;,
 &quot;Zombie Plow&quot;: &quot;åµå°¸æ¨åæº&quot;,
 &quot;ZombieRanger&quot;: &quot;åµå°¸æ¸¸ä¾ &quot;,
 &quot;Time&quot;: &quot;æ¶é´&quot;,
 &quot;Weather&quot;: &quot;å¤©æ°&quot;,
 &quot;Hour&quot;: &quot;å°æ¶&quot;,
 &quot;Apply time&quot;: &quot;åºç¨æ¶é´&quot;,
 &quot;Type&quot;: &quot;ç±»å&quot;,
 &quot;Apply weather&quot;: &quot;åºç¨å¤©æ°&quot;,
 &quot;Lock weather&quot;: &quot;éå®å¤©æ°&quot;,
 &quot;Shows the in-game clock on screen.&quot;: &quot;å¨å±å¹ä¸æ¾ç¤ºæ¸¸æåæ¶é´ã&quot;,
 &quot;Weather roulette&quot;: &quot;å¤©æ°è½®ç&quot;,
 &quot;Weather flips to a random type every couple of seconds.&quot;: &quot;æ¯éä¸¤ç§éæºæ¢ä¸æ¬¡å¤©æ°ã&quot;,
 &quot;Freeze clock&quot;: &quot;å»ç»æ¶é´&quot;,
 &quot;Time of day stays where it is.&quot;: &quot;æ¶é´åå¨å½åè¿ä¸å»ã&quot;,
 &quot;Teleport to waypoint&quot;: &quot;ä¼ éå°å¯¼èªç¹&quot;,
 &quot;No waypoint set.&quot;: &quot;è¿æ²¡æè®¾ç½®å¯¼èªç¹ã&quot;,
 &quot;Kick (host)&quot;: &quot;ä¸»æºè¸¢&quot;,
 &quot;Kick (script host)&quot;: &quot;èæ¬ä¸»æºè¸¢&quot;,
 &quot;Teleport to&quot;: &quot;ä¼ éå°ä»&quot;,
 &quot;Pull here&quot;: &quot;æå°æè¿é&quot;,
 &quot;Kick (BE)&quot;: &quot;BE è¸¢&quot;,
 &quot;Kick&quot;: &quot;è¸¢äºº&quot;,
 &quot;Mark all secondary targets as scoped.&quot;: &quot;ææ¬¡è¦ç®æ å¨é¨æ è®°ä¸ºå·²ä¾¦å¯ã&quot;,
 &quot;Mark all POIs as scouted.&quot;: &quot;æå´è¶£ç¹å¨é¨æ è®°ä¸ºå·²ä¾¦å¯ã&quot;,
 &quot;Cooldowns&quot;: &quot;å·å´ç§»é¤&quot;,
 &quot;Remove Kosatka missile cooldown&quot;: &quot;ç§»é¤èé²¸å¯¼å¼¹å·å´&quot;,
 &quot;Removes the Kosatka submarine missile cooldown.&quot;: &quot;ç§»é¤èé²¸æ½èå¯¼å¼¹å·å´ã&quot;,
 &quot;Remove appearance cooldown&quot;: &quot;ç§»é¤æ´æ¹å¤è§å·å´&quot;,
 &quot;Removes the character appearance change cooldown.&quot;: &quot;ç§»é¤æ´æ¹è§è²å¤è§çå·å´ã&quot;,
 &quot;Free appearance change&quot;: &quot;åè´¹æ´æ¹å¤è§&quot;,
 &quot;Makes appearance changes free.&quot;: &quot;æ´æ¹å¤è§ä¸åæ¶è´¹ã&quot;,
 &quot;Remove CEO work cooldown&quot;: &quot;ç§»é¤CEOå·¥ä½å·å´&quot;,
 &quot;Removes CEO work cooldowns.&quot;: &quot;ç§»é¤CEOå·¥ä½å·å´ã&quot;,
 &quot;Remove client job cooldown&quot;: &quot;ç§»é¤æé¸å®¢æ·å·®äºå·å´&quot;,
 &quot;Removes terrorbyte client job cooldowns.&quot;: &quot;ç§»é¤æé¸å®¢æ·å·®äºå·å´ã&quot;,
 &quot;Remove payphone hit cooldown&quot;: &quot;ç§»é¤ææçµè¯å·å´&quot;,
 &quot;Apartment&quot;: &quot;å¬å¯&quot;,
 &quot;Apartment heist&quot;: &quot;å¬å¯æ¢å«&quot;,
 &quot;Apply finale&quot;: &quot;åºç¨ç»ç« &quot;,
 &quot;Skip preps&quot;: &quot;è·³è¿åç½®&quot;,
 &quot;Skip pacific hack&quot;: &quot;è·³è¿å¤ªå¹³æ´ç ´è§£&quot;,
 &quot;Kortz Center&quot;: &quot;ç§å¹ä¸­å¿&quot;,
 &quot;Kortz&quot;: &quot;ç§å¹ä¸­å¿&quot;,
 &quot;Apply Kortz setup&quot;: &quot;åºç¨ç§å¹éç½®&quot;,
 &quot;Reset Kortz&quot;: &quot;éç½®ç§å¹ä¸­å¿&quot;,
 &quot;Reset finale state&quot;: &quot;æ¸ç©ºç»ç« ç¶æ&quot;,
 &quot;Read finale state&quot;: &quot;è¯»åç»ç« ç¶æ&quot;,
 &quot;Skip vault gate&quot;: &quot;è·³è¿éåºé¨ç¦&quot;,
 &quot;Skip data hack&quot;: &quot;è·³è¿æ°æ®ç ´è§£&quot;,
 &quot;Weaken guards in the finale.&quot;: &quot;ç»ç« ä¸­å¼±åä¿å®ã&quot;,
 &quot;Cayo Perico&quot;: &quot;ä½©éç§å²&quot;,
 &quot;Casino&quot;: &quot;åé»èµåº&quot;,
 &quot;Doomsday&quot;: &quot;æ«æ¥è±ªå«&quot;,
 &quot;Cayo&quot;: &quot;ä½©éç§å²&quot;,
 &quot;Cayo detector&quot;: &quot;ä½©éç§å²æ£æµå¨&quot;,
 &quot;Read Cayo stats&quot;: &quot;è¯»åä½©éç§å²æ°æ®&quot;,
 &quot;Madrazo files value&quot;: &quot;é©¬å¾·æç´¢æä»¶&quot;,
 &quot;Panther statue value&quot;: &quot;é»è±¹éå&quot;,
 &quot;Cut slot 1 (host)&quot;: &quot;åçº¢ 1ï¼ä¸»æºï¼&quot;,
 &quot;Cut slot 2&quot;: &quot;åçº¢ 2&quot;,
 &quot;Cut slot 3&quot;: &quot;åçº¢ 3&quot;,
 &quot;Cut slot 4&quot;: &quot;åçº¢ 4&quot;,
 &quot;Cut slot 1&quot;: &quot;åçº¢ 1&quot;,
 &quot;Apply cuts&quot;: &quot;åºç¨åçº¢&quot;,
 &quot;Apply casino cuts&quot;: &quot;åºç¨èµåºåçº¢&quot;,
 &quot;Apply doomsday cuts&quot;: &quot;åºç¨æ«æ¥åçº¢&quot;,
 &quot;Cayo cuts applied.&quot;: &quot;ä½©éç§å²åçº¢å·²åå¥ã&quot;,
 &quot;Casino cuts applied.&quot;: &quot;èµåºåçº¢å·²åå¥ã&quot;,
 &quot;Doomsday cuts applied.&quot;: &quot;æ«æ¥è±ªå«åçº¢å·²åå¥ã&quot;,
 &quot;Cuts the city lights around you.&quot;: &quot;å³æå¨å´çåå¸ç¯åã&quot;,
 &quot;Scanner&quot;: &quot;æ«æ&quot;,
 &quot;Hacks&quot;: &quot;éªå¥å¨ä½&quot;,
 &quot;Hack lock&quot;: &quot;éªå¥éå®&quot;,
 &quot;Profile overlay&quot;: &quot;ç®æ èµææµ®å±&quot;,
 &quot;Disarm&quot;: &quot;ç¼´æ¢°&quot;,
 &quot;Stun&quot;: &quot;æ¾å&quot;,
 &quot;Blackout&quot;: &quot;åçµ&quot;,
 &quot;HACK&quot;: &quot;éªå¥&quot;,
 &quot;Locks the ped or online player nearest the centre of your screen.&quot;: &quot;éå®å±å¹ä¸­å¿æè¿ç NPC æå¨çº¿ç©å®¶ã&quot;,
 &quot;Locks the ped, player or vehicle nearest the centre of your screen that you can actually see.&quot;: &quot;éå®å±å¹ä¸­å¿æè¿çé£ä¸ªäººæè½½å·ã&quot;,
 &quot;Quick key&quot;: &quot;å¿«æ·é®&quot;,
 &quot;Hack key&quot;: &quot;éªå¥æé®&quot;,
 &quot;Press the key below to repeat the hack you last used, without opening the menu.&quot;: &quot;æä¸é¢è¿ä¸ªé®ï¼éå¤ä¸ä¸æ¬¡çéªå¥å¨ä½ï¼è¿èåé½ä¸ç¨å¼ã&quot;,
 &quot;Remote start&quot;: &quot;è¿ç¨å¯å¨&quot;,
 &quot;Traffic jam&quot;: &quot;å µè½¦&quot;,
 &quot;Jam traffic&quot;: &quot;å¨åå µè½¦&quot;,
 &quot;Jump to target&quot;: &quot;è·³å°ç®æ èº«ä¸&quot;,
 &quot;Freeze&quot;: &quot;å»ç»ç®æ &quot;,
 &quot;Unfreeze&quot;: &quot;è§£å»&quot;,
 &quot;Panic target&quot;: &quot;è®©ç®æ éè·&quot;,
 &quot;Test scan&quot;: &quot;æµè¯æ«æ&quot;,
 &quot;Mounts&quot;: &quot;åéª&quot;,
 &quot;Thor mode&quot;: &quot;é·ç¥æ¨¡å¼&quot;,
 &quot;Iron Man mode&quot;: &quot;é¢éä¾ æ¨¡å¼&quot;,
 &quot;Enable Thor&quot;: &quot;å¼å¯é·ç¥&quot;,
 &quot;Lightning aura&quot;: &quot;é·çµåç¯&quot;,
 &quot;Show hammer&quot;: &quot;æ¾ç¤ºé¤å­&quot;,
 &quot;Hammer ground strike&quot;: &quot;é¤å­ç ¸å°&quot;,
 &quot;Lightning intensity&quot;: &quot;é·çµå¼ºåº¦&quot;,
 &quot;Disable Thor&quot;: &quot;å³é­é·ç¥&quot;,
 &quot;Enable flight&quot;: &quot;å¼å¯é£è¡&quot;,
 &quot;Flight speed&quot;: &quot;é£è¡éåº¦&quot;,
 &quot;Boost speed&quot;: &quot;é«éæ¨è¿&quot;,
 &quot;Boost multiplier&quot;: &quot;æ¨è¿åç&quot;,
 &quot;Hover&quot;: &quot;ç©ºä¸­æ¬å&quot;,
 &quot;Hand thrusters&quot;: &quot;æææ¨è¿å¨&quot;,
 &quot;Foot thrusters&quot;: &quot;èé¨æ¨è¿å¨&quot;,
 &quot;Flight animation&quot;: &quot;é£è¡å§¿å¿å¨ç»&quot;,
 &quot;Hover pose&quot;: &quot;æ¬åå§¿å¿ï¼ç´ç«ï¼&quot;,
 &quot;Emergency stop&quot;: &quot;ç´§æ¥åæ­¢&quot;,
 &quot;Disable Iron Man&quot;: &quot;å³é­é¢éä¾ &quot;,
 &quot;Key B = ground strike, V = toggle Iron Man&quot;: &quot;æé®ï¼B ç ¸å°ï¼V å¼å³é¢éä¾ &quot;,
 &quot;FX settings&quot;: &quot;ç¹æåæ°&quot;,
 &quot;Particle size&quot;: &quot;ç²å­å¤§å°&quot;,
 &quot;Particle density&quot;: &quot;ç²å­å¯åº¦&quot;,
 &quot;Effect speed&quot;: &quot;ç¹æéåº¦&quot;,
 &quot;Shockwave range&quot;: &quot;å²å»æ³¢èå´&quot;,
 &quot;Camera shake&quot;: &quot;ç¸æºéå¨&quot;,
 &quot;Shake strength&quot;: &quot;éå¨å¼ºåº¦&quot;,
 &quot;Dynamic light&quot;: &quot;å¨ææå&quot;,
 &quot;Screen flash&quot;: &quot;å±å¹éªå&quot;,
 &quot;Impact timing&quot;: &quot;å¼çæ¶æºï¼è·å¨ä½ï¼è¶å¤§è¶æï¼&quot;,
 &quot;Impact delay&quot;: &quot;å¼çå»¶æ¶ï¼æ å¨ä½æ¶ï¼&quot;,
 &quot;W/S/A/D move, Space up, Ctrl down, Shift boost&quot;: &quot;W/S/A/D ç§»å¨ï¼ç©ºæ ¼ä¸åï¼Ctrl ä¸éï¼Shift å é&quot;,
 &quot;Ride animal&quot;: &quot;éªå¨ç©&quot;,
 &quot;Dismount&quot;: &quot;ä¸é©¬&quot;,
 &quot;Animal&quot;: &quot;å¨ç©&quot;,
 &quot;Attach bone&quot;: &quot;ææ¥éª¨éª¼&quot;,
 &quot;Seat forward&quot;: &quot;åº§ä½ååå¾®è°&quot;,
 &quot;Seat side&quot;: &quot;åº§ä½å·¦å³å¾®è°&quot;,
 &quot;Tilt X&quot;: &quot;å¾æ X å¾®è°&quot;,
 &quot;Tilt Y&quot;: &quot;å¾æ Y å¾®è°&quot;,
 &quot;Tilt Z&quot;: &quot;å¾æ Z å¾®è°&quot;,
 &quot;Root&quot;: &quot;æ ¹éª¨éª¼&quot;,
 &quot;Mount speed&quot;: &quot;ç§»å¨éåº¦ï¼1èµ° 2è· 3å²åºï¼&quot;,
 &quot;Seat height&quot;: &quot;åº§ä½é«åº¦å¾®è°&quot;,
 &quot;Deer&quot;: &quot;é¹¿&quot;,
 &quot;Cow&quot;: &quot;ç&quot;,
 &quot;Pig&quot;: &quot;çª&quot;,
 &quot;Boar&quot;: &quot;éçª&quot;,
 &quot;Coyote&quot;: &quot;éç¼&quot;,
 &quot;Husky&quot;: &quot;åå£«å¥&quot;,
 &quot;Rottweiler&quot;: &quot;ç½å¨çº³&quot;,
 &quot;Mountain Lion&quot;: &quot;å±±ç®&quot;,
 &quot;Pug&quot;: &quot;å·´å¥ç¬&quot;,
 &quot;Golden Retriever&quot;: &quot;éæ¯&quot;,
 &quot;Follow target&quot;: &quot;è·éç®æ &quot;,
 &quot;Entity tricks&quot;: &quot;å®ä½æ¶æ&quot;,
 &quot;Launch (G)&quot;: &quot;èµ·é£ (G)&quot;,
 &quot;Cage (H)&quot;: &quot;å³ç¬¼å­ (H)&quot;,
 &quot;Fence cage&quot;: &quot;æ æ ç¬¼å­&quot;,
 &quot;Container cage&quot;: &quot;è´§æç¬¼å­&quot;,
 &quot;Release cage&quot;: &quot;è§£é¤å³ä½&quot;,
 &quot;Water (J)&quot;: &quot;å·æ°´ (J)&quot;,
 &quot;Fire (K)&quot;: &quot;å·ç« (K)&quot;,
 &quot;Remove cage&quot;: &quot;ææç¬¼å­&quot;,
 &quot;Explode target (R)&quot;: &quot;ç´æ¥çç¸ (R)&quot;,
 &quot;Box sticks to the target instead of the crosshair. Only turn it on if the box lands on people.&quot;: &quot;æ¡è´´å¨ç®æ èº«ä¸ï¼ä¸è·çåæè·ãåªæç¡®è®¤æ¡è½å¯¹åäººæ¶æå¼ã&quot;,
 &quot;Action keys&quot;: &quot;å¨ä½å¿«æ·é®&quot;,
 &quot;Projection&quot;: &quot;æå½±æ¹å¼&quot;,
 &quot;Vehicle hacks&quot;: &quot;è½½å·éªå¥&quot;,
 &quot;Enter (Z)&quot;: &quot;ä¸è½¦ (Z)&quot;,
 &quot;Wreck (X)&quot;: &quot;æ¥åº (X)&quot;,
 &quot;Explode (C)&quot;: &quot;ç¸è½¦ (C)&quot;,
 &quot;Repair (E)&quot;: &quot;ç»´ä¿® (E)&quot;,
 &quot;Clone (F)&quot;: &quot;åé (F)&quot;,
 &quot;Teleport (T)&quot;: &quot;ä¼ é (T)&quot;,
 &quot;Shows Z X C E F R T under the lock and runs them while a target is locked.&quot;: &quot;éå®åæ¾ç¤º Z X C E F R Tï¼éçç®æ æ¶æå°±æ§è¡ã&quot;,
 &quot;Physics&quot;: &quot;ç©ç&quot;,
 &quot;Chaos&quot;: &quot;æ··ä¹±&quot;,
 &quot;Low gravity&quot;: &quot;ä½éå&quot;,
 &quot;Gravity level&quot;: &quot;éåæ¡£ä½&quot;,
 &quot;Slow motion&quot;: &quot;æ¢å¨ä½&quot;,
 &quot;Time scale&quot;: &quot;æ¶é´åç&quot;,
 &quot;Wave radius&quot;: &quot;æ³¢å¨åå¾&quot;,
 &quot;Ragdoll wave&quot;: &quot;æ¾åå¨åº&quot;,
 &quot;Panic wave&quot;: &quot;æç¾¤&quot;,
 &quot;Earthquake&quot;: &quot;å°éï¼&quot;,
 &quot;Hop on space&quot;: &quot;ç©ºæ ¼è·³è½¦&quot;,
 &quot;Auto repair&quot;: &quot;èªå¨ä¿®è½¦&quot;,
 &quot;Everything floats around while it is on.&quot;: &quot;å¼ççæ¶åå¨å´çä¸è¥¿é½å¨é£ã&quot;,
 &quot;Slows the whole world down, you included.&quot;: &quot;æ´ä¸ªä¸çé½ä¼åæ¢ï¼åæ¬ä½ èªå·±ã&quot;,
 &quot;Press space while driving to jump.&quot;: &quot;å¼è½¦æ¶æç©ºæ ¼è·³ä¸ä¸ã&quot;,
 &quot;Your ride repairs itself while you drive.&quot;: &quot;å¼è½¦æ¶è½½å·èªå¨ä¿®å¤ã&quot;,
 &quot;Keeps stopping every car around you while it is on.&quot;: &quot;å¼ççæ¶åå¨å´çè½¦ä¸ç´è¢«å¹åã&quot;,
 &quot;Ped launch&quot;: &quot;éä¸å¤©&quot;,
 &quot;Street&quot;: &quot;è¡é&quot;,
 &quot;Icy roads&quot;: &quot;å°é¢&quot;,
 &quot;Car magnet&quot;: &quot;å¿µåå¸è½¦&quot;,
 &quot;Magnet range&quot;: &quot;å¸è½¦èå´&quot;,
 &quot;Nearby cars lose all grip.&quot;: &quot;å¨å´çè½¦å¨é¨ææ»ã&quot;,
 &quot;Drags every car around you towards you.&quot;: &quot;æå¨å´çè½¦å¨é½æ½åä½ ã&quot;,
 &quot;NPCs surrender&quot;: &quot;éè¿ NPC æé&quot;,
 &quot;Dress-up wave&quot;: &quot;æ¢è£æ³¢&quot;,
 &quot;Rainbow traffic&quot;: &quot;å½©è¹è½¦æµ&quot;,
 &quot;Super jump&quot;: &quot;è¶çº§è·³&quot;,
 &quot;Repaints every car around you with random colours.&quot;: &quot;æå¨å´æ¯è¾è½¦çé¢è²éæºéå·ã&quot;,
 &quot;Jump much higher while on foot.&quot;: &quot;æ­¥è¡æ¶è½è·³å¾ç¹å«é«ã&quot;,
 &quot;Traffic density&quot;: &quot;äº¤éå¯åº¦&quot;,
 &quot;Police ignore me&quot;: &quot;è­¦å¯æ è§æ&quot;,
 &quot;Cops stop chasing you and forget your wanted level.&quot;: &quot;è­¦å¯ä¸åè¿½ä½ ï¼éç¼ç­çº§ä¹ä¼æ¸ç©ºã&quot;,
 &quot;Force push&quot;: &quot;ååºè½°é£&quot;,
 &quot;Launch cars&quot;: &quot;æè½¦ä¸å¤©&quot;,
 &quot;Drunk camera&quot;: &quot;éééå¤´&quot;,
 &quot;The camera sways like you drank too much.&quot;: &quot;éå¤´ä¼ååå¤äºä¸æ ·æã&quot;,
 &quot;Horn blast&quot;: &quot;åå­å²å»æ³¢&quot;,
 &quot;Honk to blast everything around your car away.&quot;: &quot;æåå­æè½¦å¨å´çä¸è¥¿å¨è½°å¼ã&quot;,
 &quot;Riot&quot;: &quot;æ´å¨&quot;,
 &quot;Vortex&quot;: &quot;æ¼©æ¶¡&quot;,
 &quot;Play dead&quot;: &quot;è£æ­»&quot;,
 &quot;Freeze wave&quot;: &quot;å®èº«æ³¢&quot;,
 &quot;See-through world&quot;: &quot;ééä¸ç [!]å®éªæ§åè½&quot;,
 &quot;Restore model size&quot;: &quot;è¿åæ¨¡åå¤§å°&quot;,
 &quot;Entity limit&quot;: &quot;å®ä½æ°éä¸é&quot;,
 &quot;Big star&quot;: &quot;å¤§ææ&quot;,
 &quot;Aim slow-mo&quot;: &quot;çåæ¢å¨ä½&quot;,
 &quot;Street brawl&quot;: &quot;è¡å¤´ç«å¹¶&quot;,
 &quot;Convoy&quot;: &quot;è½¦é&quot;,
 &quot;Convoy escort&quot;: &quot;è½¦éæ¤é&quot;,
 &quot;Bodyguards invincible&quot;: &quot;ä¿éæ æ&quot;,
 &quot;Convoy vehicles invincible&quot;: &quot;ä¿éè½½å·æ æ&quot;,
 &quot;Convoy rainbow paint&quot;: &quot;ä¿éå½©è¹è½½å·&quot;,
 &quot;Convoy shot damage&quot;: &quot;ä¿éå­å¼¹ä¼¤å®³&quot;,
 &quot;Unarmed&quot;: &quot;ç©ºæ&quot;,
 &quot;Knife&quot;: &quot;å&quot;,
 &quot;Nightstick&quot;: &quot;è­¦æ£&quot;,
 &quot;Hammer&quot;: &quot;é¤å­&quot;,
 &quot;Baseball Bat&quot;: &quot;æ£çæ£&quot;,
 &quot;Crowbar&quot;: &quot;æ¬æ£&quot;,
 &quot;Golf Club&quot;: &quot;é«å°å¤«çæ&quot;,
 &quot;Bottle&quot;: &quot;éç¶&quot;,
 &quot;Cavalry Dagger&quot;: &quot;éªåµåé¦&quot;,
 &quot;Hatchet&quot;: &quot;ææ§&quot;,
 &quot;Knuckle Duster&quot;: &quot;æè&quot;,
 &quot;Machete&quot;: &quot;ç å&quot;,
 &quot;Switchblade&quot;: &quot;å¼¹ç°§å&quot;,
 &quot;Pool Cue&quot;: &quot;å°çæ&quot;,
 &quot;Wrench&quot;: &quot;æ³æ&quot;,
 &quot;Battle Axe&quot;: &quot;ææ§&quot;,
 &quot;Pistol .50&quot;: &quot;.50 ææª&quot;,
 &quot;AP Pistol&quot;: &quot;ç©¿ç²ææª&quot;,
 &quot;Combat Pistol&quot;: &quot;ææææª&quot;,
 &quot;Heavy Pistol&quot;: &quot;éåææª&quot;,
 &quot;SNS Pistol&quot;: &quot;SNS ææª&quot;,
 &quot;Vintage Pistol&quot;: &quot;å¤å¤ææª&quot;,
 &quot;Ceramic Pistol&quot;: &quot;é¶ç·ææª&quot;,
 &quot;Heavy Revolver&quot;: &quot;éåå·¦è½®&quot;,
 &quot;Double Action Revolver&quot;: &quot;åå¨å·¦è½®&quot;,
 &quot;Marksman Pistol&quot;: &quot;å°æææª&quot;,
 &quot;Navy Revolver&quot;: &quot;æµ·åå·¦è½®&quot;,
 &quot;Micro SMG&quot;: &quot;å¾®åå²éæª&quot;,
 &quot;Assault SMG&quot;: &quot;çªå»å²éæª&quot;,
 &quot;Combat PDW&quot;: &quot;ææ PDW&quot;,
 &quot;Machine Pistol&quot;: &quot;æºå³ææª&quot;,
 &quot;Mini SMG&quot;: &quot;è¿·ä½ å²éæª&quot;,
 &quot;Assault Rifle&quot;: &quot;çªå»æ­¥æª&quot;,
 &quot;Carbine Rifle&quot;: &quot;å¡å®¾æ­¥æª&quot;,
 &quot;Advanced Rifle&quot;: &quot;é«çº§æ­¥æª&quot;,
 &quot;Special Carbine&quot;: &quot;ç¹ç§å¡å®¾&quot;,
 &quot;Bullpup Rifle&quot;: &quot;æ ææ­¥æª&quot;,
 &quot;Compact Rifle&quot;: &quot;ç´§åæ­¥æª&quot;,
 &quot;Military Rifle&quot;: &quot;åç¨æ­¥æª&quot;,
 &quot;Heavy Rifle&quot;: &quot;éåæ­¥æª&quot;,
 &quot;Pump Shotgun&quot;: &quot;æ³µå¨é°å¼¹æª&quot;,
 &quot;Sawed-Off Shotgun&quot;: &quot;ç­ç®¡é°å¼¹æª&quot;,
 &quot;Assault Shotgun&quot;: &quot;çªå»é°å¼¹æª&quot;,
 &quot;Bullpup Shotgun&quot;: &quot;æ æé°å¼¹æª&quot;,
 &quot;Heavy Shotgun&quot;: &quot;éåé°å¼¹æª&quot;,
 &quot;Double Barrel Shotgun&quot;: &quot;åç®¡é°å¼¹æª&quot;,
 &quot;Sweeper Shotgun&quot;: &quot;æ«å°é°å¼¹æª&quot;,
 &quot;Musket&quot;: &quot;ç«æª&quot;,
 &quot;MG&quot;: &quot;æºæª&quot;,
 &quot;Combat MG&quot;: &quot;æææºæª&quot;,
 &quot;Gusenberg Sweeper&quot;: &quot;å¤æ£®ä¼¯æ ¼å²éæª&quot;,
 &quot;Sniper Rifle&quot;: &quot;çå»æ­¥æª&quot;,
 &quot;Heavy Sniper&quot;: &quot;éåçå»æª&quot;,
 &quot;Marksman Rifle&quot;: &quot;å°ææ­¥æª&quot;,
 &quot;Grenade Launcher&quot;: &quot;æ¦´å¼¹åå°å¨&quot;,
 &quot;Firework Launcher&quot;: &quot;çè±åå°å¨&quot;,
 &quot;Homing Launcher&quot;: &quot;è¿½è¸ªå¯¼å¼¹åå°å¨&quot;,
 &quot;Compact Launcher&quot;: &quot;ç´§åæ¦´å¼¹åå°å¨&quot;,
 &quot;Railgun&quot;: &quot;è½¨éç®&quot;,
 &quot;Grenade&quot;: &quot;æé·&quot;,
 &quot;Sticky Bomb&quot;: &quot;ç²å¼¹&quot;,
 &quot;Smoke Grenade&quot;: &quot;çé¾å¼¹&quot;,
 &quot;Molotov&quot;: &quot;çç§ç¶&quot;,
 &quot;Pipe Bomb&quot;: &quot;åå¶ç¸å¼¹&quot;,
 &quot;Flare&quot;: &quot;ä¿¡å·å¼¹&quot;,
 &quot;Snowball&quot;: &quot;éªç&quot;,
 &quot;ESP&quot;: &quot;ESP&quot;,
 &quot;Enable ESP&quot;: &quot;å¼å¯éè§&quot;,
 &quot;Snaplines&quot;: &quot;å¼å¯¼çº¿&quot;,
 &quot;Skeleton&quot;: &quot;éª¨éª¼&quot;,
 &quot;Box&quot;: &quot;æ¹æ¡&quot;,
 &quot;Health bar&quot;: &quot;è¡æ¡&quot;,
 &quot;Armor bar&quot;: &quot;æ¤ç²æ¡&quot;,
 &quot;Name&quot;: &quot;åå­&quot;,
 &quot;Wanted&quot;: &quot;éç¼&quot;,
 &quot;Level&quot;: &quot;ç­çº§&quot;,
 &quot;Cash&quot;: &quot;ç°é&quot;,
 &quot;ESP range&quot;: &quot;éè§èå´&quot;,
 &quot;No limit&quot;: &quot;æ ä¸é&quot;,
 &quot;Visible color&quot;: &quot;å¯è§é¢è²&quot;,
 &quot;Invisible color&quot;: &quot;ä¸å¯è§é¢è²&quot;,
 &quot;Distance&quot;: &quot;è·ç¦»&quot;,
 &quot;Text background&quot;: &quot;æå­åºè²&quot;,
 &quot;Skip indoor&quot;: &quot;å±è½å®¤å&quot;,
 &quot;Snapline color&quot;: &quot;å¼å¯¼çº¿é¢è²&quot;,
 &quot;Box color&quot;: &quot;æ¹æ¡é¢è²&quot;,
 &quot;Skeleton color&quot;: &quot;éª¨éª¼é¢è²&quot;,
 &quot;Select all&quot;: &quot;å¨é&quot;,
 &quot;Saved places&quot;: &quot;åæ æ¶è&quot;,
 &quot;Profiles&quot;: &quot;å­æ¡£æ¡£ä½&quot;,
 &quot;Save current place&quot;: &quot;ä¿å­å½åä½ç½®&quot;,
 &quot;Delete last place&quot;: &quot;å é¤æåä¸ä¸ª&quot;,
 &quot;Save profile&quot;: &quot;ä¿å­æ¡£ä½&quot;,
 &quot;Load profile 1&quot;: &quot;è¯»åæ¡£ä½ 1&quot;,
 &quot;Double-click a folder to expand, double-click a point to teleport.&quot;: &quot;åå»æ ç®å±å¼ï¼åå»ç¹ä½ä¼ éã&quot;,
 &quot;No saved places yet.&quot;: &quot;è¿æ²¡æä¿å­çåæ ã&quot;,
 &quot;Landmarks&quot;: &quot;å°æ &quot;,
 &quot;Airport&quot;: &quot;æºåº&quot;,
 &quot;Mount Chiliad&quot;: &quot;å¥åè¶å¾·å±±&quot;,
 &quot;Vinewood Sign&quot;: &quot;å¥½è±åæ å¿&quot;,
 &quot;Del Perro Pier&quot;: &quot;ä½©ç½ç å¤´&quot;,
 &quot;Fort Zancudo&quot;: &quot;æ¡åºå¤åè¥&quot;,
 &quot;Sandy Shores&quot;: &quot;æ²å°æµ·å²¸&quot;,
 &quot;Clear&quot;: &quot;æ¸é¤&quot;,
 &quot;Interface, language, config file, and about.&quot;: &quot;çé¢ãè¯­è¨ãéç½®æä»¶ä¸å³äºã&quot;,
 &quot;Interface&quot;: &quot;çé¢&quot;,
 &quot;Accent&quot;: &quot;ä¸»é¢è²&quot;,
 &quot;Keys&quot;: &quot;æé®&quot;,
 &quot;Config&quot;: &quot;éç½®&quot;,
 &quot;About&quot;: &quot;å³äº&quot;,
 &quot;Language&quot;: &quot;è¯­è¨&quot;,
 &quot;Push toast&quot;: &quot;å¼¹åºæç¤º&quot;,
 &quot;Save config&quot;: &quot;ä¿å­éç½®&quot;,
 &quot;UI scale&quot;: &quot;çé¢ç¼©æ¾&quot;,
 &quot;Toast notifications&quot;: &quot;æç¤ºæ°æ³¡&quot;,
 &quot;Animated toasts bottom right.&quot;: &quot;å³ä¸è§çå¨ç»æç¤ºã&quot;,
 &quot;Font Awesome icons&quot;: &quot;å¾æ &quot;,
 &quot;Turn off if glyphs render as boxes.&quot;: &quot;å¾æ æ¾ç¤ºææ¹åæ¶å³æã&quot;,
 &quot;Debug overlay&quot;: &quot;è°è¯ä¿¡æ¯&quot;,
 &quot;Shows a small status readout in the top-left corner.&quot;: &quot;å¨å·¦ä¸è§æ¾ç¤ºä¸è¡ç¶æä¿¡æ¯ã&quot;,
 &quot;Colour&quot;: &quot;ä¸»é¢è²&quot;,
 &quot;Menu key&quot;: &quot;èåé®&quot;,
 &quot;Save&quot;: &quot;ä¿å­&quot;,
 &quot;Reload&quot;: &quot;éæ°å è½½&quot;,
 &quot;Reset window&quot;: &quot;éç½®çªå£&quot;,
 &quot;Show path&quot;: &quot;æ¾ç¤ºè·¯å¾&quot;,
 &quot;Reset to defaults&quot;: &quot;æ¢å¤é»è®¤&quot;,
 &quot;FILTER&quot;: &quot;ç­é&quot;,
 &quot;Error&quot;: &quot;éè¯¯&quot;,
 &quot;natives.lua not loaded (require failed)&quot;: &quot;natives.lua å è½½å¤±è´¥ï¼require åºéï¼&quot;,
 &quot;natives.lua not available (missing file or natives permission)&quot;: &quot;natives.lua ä¸å¯ç¨ï¼ç¼ºå°æä»¶ææ²¡æ natives æéï¼&quot;,
 &quot;Config reloaded.&quot;: &quot;éç½®å·²éæ°å è½½ã&quot;,
 &quot;Every pixel is gui.rect / gui.text â no outline, no circle.&quot;: &quot;æ¯ä¸ªåç´ é½æ¯ gui.rect / gui.text ââ ä¸ç¨ outlineï¼ä¸ç¨ circleã&quot;,
 &quot;toast.loaded&quot;: &quot;å·²å è½½ï¼æ %s æå¼ã&quot;,
 &quot;toast.hello&quot;: &quot;æ¥èª %s çé®åã&quot;,
 &quot;toast.cfgsave&quot;: &quot;éç½®å·²ä¿å­ï¼%s&quot;,
 &quot;toast.cfgfail&quot;: &quot;éç½®ä¿å­å¤±è´¥ï¼%s&quot;,
 &quot;toast.cfgdisabled&quot;: &quot;éç½®è¯»åå·²ç¦ç¨ã&quot;,
 &quot;toast.invis.on&quot;: &quot;éèº«ï¼å¼&quot;,
 &quot;toast.invis.off&quot;: &quot;éèº«ï¼å³&quot;,
 &quot;toast.stats&quot;: &quot;å·²åºç¨è¡éä¸æ¤ç²ã&quot;,
 &quot;toast.wanted&quot;: &quot;éç¼ç­çº§å·²æ¸é¤ã&quot;,
 &quot;toast.tp.ok&quot;: &quot;å·²ä¼ éå°å¯¼èªç¹ã&quot;,
 &quot;toast.tp.fail&quot;: &quot;ä¼ éå¤±è´¥ï¼%s&quot;,
 &quot;toast.time&quot;: &quot;æ¶é´å·²è®¾ä¸º %02d:00ã&quot;,
 &quot;toast.weather&quot;: &quot;å¤©æ°ï¼%s&quot;,
 &quot;toast.tpplayer&quot;: &quot;å·²ä¼ éå°ç©å®¶ %s&quot;,
 &quot;toast.windowreset&quot;: &quot;çªå£ä½ç½®å·²éç½®ã&quot;,
 &quot;toast.lang&quot;: &quot;è¯­è¨ï¼%s&quot;,
 &quot;toast.langfallback&quot;: &quot;æ²¡æ¾å°ä¸­æå­ä½ï¼å·²åéè±æã&quot;,
 &quot;toast.cfgpath&quot;: &quot;éç½®æä»¶&quot;,
 &quot;toast.noplayer&quot;: &quot;è¯¥ç©å®¶å·²ç¦»å¼æå±ã&quot;,
 &quot;cfg.synced&quot;: &quot;å·²åæ­¥&quot;,
 &quot;cfg.pending&quot;: &quot;ææªä¿å­æ¹å¨&quot;,
 &quot;cfg.broken&quot;: &quot;éç½®ä¸å¯ç¨&quot;,
 &quot;toast.defaults&quot;: &quot;è®¾ç½®å·²æ¢å¤é»è®¤ï¼åæ  / å­æ¡£ / åçº¢ä¿æä¸åï¼ã&quot;,
 &quot;Only show tooltips&quot;: &quot;ä»æ¾ç¤ºæç¤ºæ¡&quot;,
 &quot;HUD&quot;: &quot;HUD&quot;,
 &quot;Watermark corner&quot;: &quot;æ°´å°ä½ç½®&quot;,
 &quot;Notifications&quot;: &quot;éç¥&quot;,
 &quot;Position&quot;: &quot;ä½ç½®&quot;,
 &quot;Increase Kosatka missile range&quot;: &quot;å¢å èé²¸å¯¼å¼¹å°ç¨&quot;,
 &quot;Raises Kosatka missile range to 99999.&quot;: &quot;æèé²¸å¯¼å¼¹å°ç¨æåå° 99999ã&quot;,
 &quot;Clear map notifications&quot;: &quot;æ¸ç©ºå°å¾éç¥&quot;,
 &quot;Only show tooltip notifications; all other map notifications are hidden.&quot;: &quot;åªçå¯¹è¯/ä»»å¡ç±»æç¤ºï¼å°å¾ä¸å¶å®éç¥å¨ç»ä½ æ¸å¹²åã&quot;,
 &quot;Presets&quot;: &quot;ä¼ éé¢è®¾&quot;,
 &quot;Cold-gas thrusters: hold TAB to launch forward, hold C to thrust backward, TAB+Space to jump straight up. Pressing TAB and C together does nothing.&quot;: &quot;å·æ°æ¨è¿å¨ï¼æä½ TAB åæ¨ãæä½ C åæ¨ãTAB+ç©ºæ ¼ åç´èµ·è·³ï¼TAB å C åæ¶æä¸çæã&quot;,
 &quot;Local swords&quot;: &quot;æ¬å°å è½½å&quot;,
 &quot;Turn this on if the swords do not show up. Off = normal mode.&quot;: &quot;åä¸æ¾ç¤ºæ¶æå¼è¿ä¸ªãå³é­ = æ­£å¸¸æ¨¡å¼ã&quot;,
 &quot;Clock&quot;: &quot;æ¶é&quot;,
 &quot;Host info&quot;: &quot;ä¸»æºä¿¡æ¯&quot;,
 &quot;Watermark&quot;: &quot;æ°´å°&quot;,
 &quot;Opacity&quot;: &quot;éæåº¦&quot;,
 &quot;Max shown&quot;: &quot;æå¤æ¾ç¤º&quot;,
 &quot;Splash&quot;: &quot;å¼å±æ¬¢è¿&quot;,
 &quot;Splash opacity&quot;: &quot;å¼å±ä¸éæåº¦&quot;,
 &quot;Test splash&quot;: &quot;æµè¯å¼å±&quot;,
 &quot;Back to list&quot;: &quot;è¿ååè¡¨&quot;,
 &quot;Player ped not available.&quot;: &quot;æ¿ä¸å°è¯¥ç©å®¶çå®ä½ã&quot;,
 &quot;Pulled to you.&quot;: &quot;å·²æå°ä½ èº«è¾¹ã&quot;,
 &quot;Pull failed.&quot;: &quot;æåå¤±è´¥ã&quot;,
 &quot;Pistol&quot;: &quot;ææª&quot;,
 &quot;SMG&quot;: &quot;å²éæª&quot;,
 &quot;Carbine rifle&quot;: &quot;å¡å®¾æª&quot;,
 &quot;Shotgun&quot;: &quot;é°å¼¹æª&quot;,
 &quot;Sniper rifle&quot;: &quot;çå»æª&quot;,
 &quot;RPG&quot;: &quot;RPG&quot;,
 &quot;Minigun&quot;: &quot;å ç¹æ&quot;,
 &quot;Top right&quot;: &quot;å³ä¸&quot;,
 &quot;Top left&quot;: &quot;å·¦ä¸&quot;,
 &quot;Bottom right&quot;: &quot;å³ä¸&quot;,
 &quot;Bottom left&quot;: &quot;å·¦ä¸&quot;,
 &quot;Indigo&quot;: &quot;éç´«&quot;,
 &quot;Cyan&quot;: &quot;éè²&quot;,
 &quot;Emerald&quot;: &quot;ç¿ ç»¿&quot;,
 &quot;Amber&quot;: &quot;ç¥ç&quot;,
 &quot;Rose&quot;: &quot;ç«ç°&quot;,
 &quot;Sort&quot;: &quot;æåº&quot;,
 &quot;Filter&quot;: &quot;è¿æ»¤&quot;,
 &quot;Max rows&quot;: &quot;æå¤æ¾ç¤º&quot;,
 &quot;Flash&quot;: &quot;éªçµä¾ &quot;,
 &quot;Flash speed&quot;: &quot;éªçµåç&quot;,
 &quot;Multiplies your sprint speed only (walking stays normal).&quot;: &quot;åªæ¾å¤§å²åºéåº¦ï¼èµ°è·¯éåº¦ä¸åï¼ã&quot;,
 &quot;Rainbow gun&quot;: &quot;å½©è¹æª&quot;,
 &quot;Laser version&quot;: &quot;æ¿åç¼çæ¬&quot;,
 &quot;Shoots wherever you look. Tip: fire with X only, and pick the version below.&quot;: &quot;æä½ ççæ¹åå¼ç«ãæç¤ºï¼åªç¨ X å¼æªï¼ä¸é¢å¯ä»¥éçæ¬ã&quot;,
 &quot;No effect â this point probably needs its mission instance.&quot;: &quot;æ²¡æçæï¼è¿ä¸ªç¹ä½å¯è½éè¦åè¿å¥å¯¹åºä»»å¡åºæ¯ã&quot;,
 &quot;Not in game.&quot;: &quot;ä¸å¨æ¸¸æéã&quot;,
 &quot;Bad coordinates.&quot;: &quot;åæ æ æã&quot;,
 &quot;Force ready&quot;: &quot;å¼ºå¶åå¤&quot;,
 &quot;Unlock board&quot;: &quot;è§£éè®¡åæ¿&quot;,
 &quot;Skip snake&quot;: &quot;è·³è¿è´ªåè&quot;,
 &quot;Skip drill&quot;: &quot;è·³è¿é»å­&quot;,
 &quot;Quick finish&quot;: &quot;å¿«éå®æ&quot;,
 &quot;Criminal mastermind&quot;: &quot;ç¯ç½ªä¹ç¥&quot;,
 &quot;Primary target&quot;: &quot;ä¸»è¦ç®æ &quot;,
 &quot;Difficulty&quot;: &quot;é¾åº¦&quot;,
 &quot;Entry&quot;: &quot;å¥ä¾µæ¹å¼&quot;,
 &quot;Loadout&quot;: &quot;æ­¦å¨å¥è£&quot;,
 &quot;Getaway&quot;: &quot;éç¦»è½½å·&quot;,
 &quot;Manchez color&quot;: &quot;æ¼åå¹é¢è²&quot;,
 &quot;Guard routes&quot;: &quot;å·¡é»è·¯çº¿&quot;,
 &quot;Glass cutter&quot;: &quot;ç»çåå²å¨&quot;,
 &quot;Power drills&quot;: &quot;çµé»&quot;,
 &quot;EMP device&quot;: &quot;çµç£èå²è£ç½®&quot;,
 &quot;Weak guards&quot;: &quot;å¼±åä¿å®&quot;,
 &quot;Scope secondary&quot;: &quot;ä¾¦å¯æ¬¡è¦ç®æ &quot;,
 &quot;Scope POIs&quot;: &quot;ä¾¦å¯å´è¶£ç¹&quot;,
 &quot;Refresh board&quot;: &quot;å·æ°è®¡åæ¿&quot;,
 &quot;Infinite lives&quot;: &quot;æ éçå½æ°&quot;,
 &quot;Head&quot;: &quot;å¤´&quot;,
 &quot;Mask&quot;: &quot;é¢å·&quot;,
 &quot;Hair&quot;: &quot;å¤´å&quot;,
 &quot;Torso&quot;: &quot;ä¸èº«&quot;,
 &quot;Legs&quot;: &quot;è¿&quot;,
 &quot;Bag&quot;: &quot;å&quot;,
 &quot;Shoes&quot;: &quot;é&quot;,
 &quot;Accessory&quot;: &quot;é¥°å&quot;,
 &quot;Undershirt&quot;: &quot;åè¡¬&quot;,
 &quot;Armor&quot;: &quot;æ¤ç²&quot;,
 &quot;Decals&quot;: &quot;è´´è±&quot;,
 &quot;Top&quot;: &quot;å¤å¥&quot;,
 &quot;# object guid=&quot;: &quot;# å¯¹è±¡ guid=&quot;,
 &quot;Radius&quot;: &quot;åå¾&quot;,
 &quot;Skip fingerprint&quot;: &quot;è·³è¿æçº¹é¨ç¦&quot;,
 &quot;Remove laser grid&quot;: &quot;ç§»é¤æ¿åç½&quot;,
 &quot;Cut glass 100%&quot;: &quot;ç»çåå²100%&quot;,
 &quot;Accelerate primary&quot;: &quot;å éä¸»è¦ç®æ &quot;,
 &quot;Accelerate secondary&quot;: &quot;å éæ¬¡è¦ç®æ &quot;,
 &quot;Infinite bag&quot;: &quot;æ éèå&quot;,
 &quot;Unlock gallery&quot;: &quot;è§£éç»å»&quot;,
 &quot;Secondary income&quot;: &quot;æ¬¡è¦ç®æ æ¶å¥&quot;,
 &quot;Set secondary income&quot;: &quot;è®¾ç½®æ¬¡è¦ç®æ æ¶å¥&quot;,
 &quot;Payout&quot;: &quot;åçº¢&quot;,
 &quot;Auxiliary&quot;: &quot;è¾å©åè½&quot;,
 &quot;Write target stats&quot;: &quot;åå¥ç®æ æ°æ®&quot;,
 &quot;Global XP = 1&quot;: &quot;å¨çå£°æ=1&quot;,
 &quot;Tequila value&quot;: &quot;è¥¿è¥¿ç±³æé¾èå°&quot;,
 &quot;Pearl necklace value&quot;: &quot;çº¢å®ç³é¡¹é¾&quot;,
 &quot;Bearer bonds value&quot;: &quot;ä¸è®°ååºå¸&quot;,
 &quot;Pink diamond value&quot;: &quot;ç²é»&quot;,
 &quot;Clear on-screen help&quot;: &quot;æ¸çå±å¹æç¤º&quot;,
 &quot;Cleared.&quot;: &quot;å·²æ¸çã&quot;,
 &quot;City&quot;: &quot;åå¸&quot;,
 &quot;Scan range&quot;: &quot;æ«æèå´&quot;,
 &quot;Aim box&quot;: &quot;çåæ¡å¤§å°&quot;,
 &quot;Read profile&quot;: &quot;è¯»åèµæ&quot;,
 &quot;Blow up car&quot;: &quot;å¼çè½½å·&quot;,
 &quot;Draws the lock bracket and a small profile next to the target.&quot;: &quot;å¨ç®æ èº«ä¸ç»éå®æ¡åä¸è¡å°èµæã&quot;,
 &quot;Police&quot;: &quot;è­¦å¯&quot;,
 &quot;Gang&quot;: &quot;å¸®æ´¾&quot;,
 &quot;Army&quot;: &quot;åé&quot;,
 &quot;SWAT&quot;: &quot;ç¹è­¦&quot;,
 &quot;Civilian&quot;: &quot;å¹³æ°&quot;,
 &quot;You never run out of reserve ammo.&quot;: &quot;å¤ç¨å¼¹è¯ä¸åã&quot;,
 &quot;Your magazines refill themselves.&quot;: &quot;å¼¹å¤¹èªå¨è¡¥æ»¡ã&quot;,
 &quot;Stop shaking&quot;: &quot;åæ­¢æå¨&quot;,
 &quot;Time crawls while you hold the aim button.&quot;: &quot;æä½çåï¼æ¶é´å°±å¼å§ç¬ã&quot;,
 &quot;Guide line&quot;: &quot;å¼å¯¼çº¿&quot;,
 &quot;Window opacity&quot;: &quot;çªå£ä¸éæåº¦&quot;,
 &quot;HUD opacity&quot;: &quot;HUD ä¸éæåº¦&quot;,
 &quot;Rainbow accent&quot;: &quot;å½©è¹ä¸»é¢è²&quot;,
 &quot;The accent colour cycles through the rainbow. Tip: turn it off to go back to the colour picked above.&quot;: &quot;å¼ºè°è²ä¼åå½©è¹ä¸æ ·æµå¨ãå³æå°±åå°ä¸é¢éçåºå®é¢è²ã&quot;,
 &quot;Anti-crash&quot;: &quot;é²å´©&quot;,
 &quot;Anti-crash camera&quot;: &quot;é²å´©éå¤´&quot;,
 &quot;Cancel sync&quot;: &quot;åæ¶åæ­¥&quot;,
 &quot;Nearby vehicles slide around as if they were on ice.&quot;: &quot;éè¿çè½½å·ä¼åå¨å°é¢ä¸æ»è¡ã&quot;,
 &quot;Summon lightning&quot;: &quot;å¬å¤éªçµ&quot;,
 &quot;Wind speed&quot;: &quot;é£é&quot;,
 &quot;Remove rain and snow&quot;: &quot;å é¤é¨éª&quot;,
 &quot;Sync real time&quot;: &quot;åæ­¥ç°å®æ¶é´&quot;,
 &quot;Keeps the in-game clock following your computer's local time.&quot;: &quot;è®©æ¸¸æåæ¶é´æç»­è·éä½ çµèçæ¬å°æ¶é´ã&quot;,
 &quot;Clock speed&quot;: &quot;æ¶é´æµé&quot;,
 &quot;NPC&quot;: &quot;NPC&quot;,
 &quot;Kill NPCs&quot;: &quot;ææ­»éè¿NPC&quot;,
 &quot;Kill enemies&quot;: &quot;ææ­»éè¿æäºº&quot;,
 &quot;Kill all NPCs&quot;: &quot;ææ­»ææ NPC&quot;,
 &quot;Kill all enemies&quot;: &quot;ææ­»æææäºº&quot;,
 &quot;Delete nearby enemies&quot;: &quot;å é¤éè¿æäºº&quot;,
 &quot;Delete all enemies&quot;: &quot;å é¤æææäºº&quot;,
 &quot;Auto kill NPCs&quot;: &quot;èªå¨ææ­»éè¿NPC&quot;,
 &quot;Auto kill enemies&quot;: &quot;èªå¨ææ­»éè¿æäºº&quot;,
 &quot;Kills NPCs inside the radius every second.&quot;: &quot;æ¯ç§ææåå¾åçææ NPCã&quot;,
 &quot;Kills only NPCs that are fighting you, every second.&quot;: &quot;æ¯ç§åªæææ­£å¨åä½ äº¤ç«/å¼æªç NPCã&quot;,
 &quot;Remove bodies&quot;: &quot;ç§»é¤å°¸ä½&quot;,
 &quot;Give all weapons&quot;: &quot;ç»äºæææ­¦å¨&quot;,
 &quot;Remove weapons&quot;: &quot;ç§»é¤NPCæææ­¦å¨&quot;,
 &quot;Knock him down&quot;: &quot;æç»­å»å&quot;,
 &quot;Environment&quot;: &quot;ç¯å¢&quot;,
 &quot;Soul&quot;: &quot;çµé­&quot;,
 &quot;Soul speed&quot;: &quot;çµé­éåº¦&quot;,
 &quot;Out of body&quot;: &quot;çµé­åºçª&quot;,
 &quot;Remove air defences&quot;: &quot;ç§»é¤é²ç©ºé¢å&quot;,
 &quot;Remove cameras&quot;: &quot;ç§»é¤éè¿æåå¤´&quot;,
 &quot;Remove all cameras&quot;: &quot;ç§»é¤æææåå¤´&quot;,
 &quot;Speed cap&quot;: &quot;éåº¦ä¸é&quot;,
 &quot;Hold Space to jump continuously; hold Shift too to build speed with each jump.&quot;: &quot;æä½ç©ºæ ¼è¿ç»­èµ·è·³ï¼åæ¶æä½ Shift ä¼éè·³è·æ¬¡æ°ç´¯å éåº¦ï¼è·³å° 100 æ¬¡åæ»¡éåº¦ä¸éã&quot;,
 &quot;Kill aura&quot;: &quot;ææ®åç¯&quot;,
 &quot;Scatter radius&quot;: &quot;æ£å¸åå¾&quot;,
 &quot;Spectate&quot;: &quot;è§å¯&quot;,
 &quot;Observe player&quot;: &quot;è§å¯ç©å®¶&quot;,
 &quot;Background&quot;: &quot;èæ¯&quot;,
 &quot;Background image&quot;: &quot;èæ¯å¾&quot;,
 &quot;Image&quot;: &quot;å¾ç&quot;,
 &quot;Refresh list&quot;: &quot;å·æ°åè¡¨&quot;,
 &quot;Background dim&quot;: &quot;èæ¯åæ&quot;,
 &quot;Fills the menu with a picture from Reverie\\UI, stretched to fit.&quot;: &quot;ç¨ Reverie\\UI éçå¾çéºæ»¡èåèæ¯ï¼èªå¨æä¼¸å¡«æ»¡ã&quot;,
 &quot;Filters&quot;: &quot;æ»¤é&quot;,
 &quot;Clear vision filter&quot;: &quot;å é¤å½åæ»¤é&quot;,
 &quot;Keep clearing filters&quot;: &quot;æç»­å é¤æ»¤é&quot;,
 &quot;Clear camera distortion&quot;: &quot;å é¤éå¤´ç¸å&quot;,
 &quot;Keep clearing distortion&quot;: &quot;æç»­æ¸çç¸å&quot;,
 &quot;PRESS KEY&quot;: &quot;æä»»æé®&quot;,
 &quot;Whoever aims at you gets blasted when you die.&quot;: &quot;æ­»äº¡æ¶ï¼æ­£å¨çä½ çäººä¼ä¸èµ·è¢«å¸¦èµ°ã&quot;,
 &quot;Show a welcome card on load.&quot;: &quot;æå¼èåæ¶æ¾ç¤ºä¸å¼ æ¬¢è¿å¡çã&quot;,
 &quot;Saved current place.&quot;: &quot;å·²ä¿å­å½åä½ç½®ã&quot;,
 &quot;Profile saved.&quot;: &quot;éç½®æä»¶å·²ä¿å­ã&quot;,
 &quot;Loaded %s.&quot;: &quot;å·²å è½½ %sã&quot;,
 &quot;Water platform model could not be created.&quot;: &quot;æ°´é¢å¹³å°æ¨¡ååå»ºå¤±è´¥ã&quot;,
 &quot;TP %s -&gt; %.0f, %.0f, %.0f&quot;: &quot;ä¼ é %s â %.0f, %.0f, %.0f&quot;,
 &quot;Doomsday Heist&quot;: &quot;æ«æ¥è±ªå«&quot;,
 &quot;Los Santos&quot;: &quot;æ´å£é½&quot;,
 &quot;Submarine&quot;: &quot;æ½è&quot;,
 &quot;Strategic bomber&quot;: &quot;æç¥è½°ç¸æº&quot;,
 &quot;Smuggler plane&quot;: &quot;èµ°ç§é£æº&quot;,
 &quot;Stealth heli&quot;: &quot;éèº«ç´åæº&quot;,
 &quot;Patrol boat&quot;: &quot;å·¡é»è&quot;,
 &quot;Smuggler boat&quot;: &quot;èµ°ç§è¹&quot;,
 &quot;Unknown Cayo target: &quot;: &quot;æªç¥çä½©éç§ç®æ ï¼&quot;,
 &quot;Cayo payout -&gt; %d (x4)&quot;: &quot;ä½©éç§æ¶ç â %dï¼Ã4ï¼&quot;,
 &quot;Casino target not set.&quot;: &quot;æªè®¾ç½®èµåºç®æ ã&quot;,
 &quot;Casino payout -&gt; %d%% (x4)&quot;: &quot;èµåºæ¶ç â %d%%ï¼Ã4ï¼&quot;,
 &quot;Vault amount -&gt; %d&quot;: &quot;éåºéé¢ â %d&quot;,
 &quot;Casino finish -&gt; %d locals&quot;: &quot;èµåºæ¶å°¾ â %d&quot;,
 &quot;No local player id.&quot;: &quot;è¯»ä¸å°æ¬å°ç©å®¶ idã&quot;,
 &quot;Vault countdown set.&quot;: &quot;éåºåè®¡æ¶å·²è®¾ç½®ã&quot;,
 &quot;Global write failed.&quot;: &quot;å¨å±åéåå¥å¤±è´¥ã&quot;,
 &quot;Casino keypad -&gt; %d locals&quot;: &quot;èµåºé®ç â %d&quot;,
 &quot;Casino double door unlocked.&quot;: &quot;èµåºåé¨å·²è§£éã&quot;,
 &quot;Door write failed.&quot;: &quot;é¨ç¶æåå¥å¤±è´¥ã&quot;,
 &quot;Vault drill state unreadable.&quot;: &quot;è¯»ä¸å°éåºé»æºç¶æã&quot;,
 &quot;Vault drill skipped.&quot;: &quot;å·²è·³è¿éåºé»æºã&quot;,
 &quot;Local write failed.&quot;: &quot;æ¬å°åéåå¥å¤±è´¥ã&quot;,
 &quot;Doomsday progress unknown: &quot;: &quot;æ«æ¥è¿åº¦æªç¥ï¼&quot;,
 &quot;Doomsday payout -&gt; %s %s: %d&quot;: &quot;æ«æ¥æ¶ç â %s %sï¼%d&quot;,
 &quot;Terminal hack skip -&gt; %d locals&quot;: &quot;ç»ç«¯éªå¥å·²è·³è¿ â %d&quot;,
 &quot;No Cayo target set.&quot;: &quot;æªè®¾ç½®ä½©éç§ç®æ ã&quot;,
 &quot;Take primary -&gt; %d locals&quot;: &quot;æ¿åä¸»è¦ç®æ  â %d&quot;,
 &quot;Cayo double door unlocked.&quot;: &quot;ä½©éç§åé¨å·²è§£éã&quot;,
 &quot;Cayo target stats -&gt; %d written&quot;: &quot;ä½©éç§ç®æ ç»è®¡ â å·²åå¥ %d é¡¹&quot;,
 &quot;Global XP set to 1.&quot;: &quot;å¨å±ç»éªå·²è®¾ä¸º 1ã&quot;,
 &quot;Stat write failed.&quot;: &quot;ç»è®¡åå¥å¤±è´¥ã&quot;,
 &quot;EXTRASUNNY&quot;: &quot;æ´ç©ºä¸é&quot;,
 &quot;CLEAR&quot;: &quot;æ´æ&quot;,
 &quot;CLOUDS&quot;: &quot;å¤äº&quot;,
 &quot;OVERCAST&quot;: &quot;é´å¤©&quot;,
 &quot;RAIN&quot;: &quot;å°é¨&quot;,
 &quot;CLEARING&quot;: &quot;é¨è¿å¤©æ´&quot;,
 &quot;THUNDER&quot;: &quot;é·é¨&quot;,
 &quot;SMOG&quot;: &quot;é¾é¾&quot;,
 &quot;FOGGY&quot;: &quot;å¤§é¾&quot;,
 &quot;SNOW&quot;: &quot;å°éª&quot;,
 &quot;BLIZZARD&quot;: &quot;æ´é£éª&quot;,
 &quot;XMAS&quot;: &quot;å£è¯&quot;,
 &quot;HALLOWEEN&quot;: &quot;ä¸å£è&quot;,
 &quot;NEUTRAL&quot;: &quot;ä¸­æ§&quot;,
 &quot;SNOWLIGHT&quot;: &quot;èéª&quot;,
 &quot;Chat&quot;: &quot;èå¤©&quot;,
 &quot;Chatroom&quot;: &quot;èå¤©å®¤&quot;,
 &quot;Say&quot;: &quot;åè¨&quot;,
 &quot;Nick&quot;: &quot;æµç§°&quot;,
 &quot;Nickname&quot;: &quot;æµç§°&quot;,
 &quot;Set nick&quot;: &quot;åºç¨æµç§°&quot;,
 &quot;Send&quot;: &quot;åé&quot;,
 &quot;History&quot;: &quot;åå²&quot;,
 &quot;messages&quot;: &quot;æ¡æ¶æ¯&quot;,
 &quot;â online&quot;: &quot;â å¨çº¿&quot;,
 &quot;â offline&quot;: &quot;â ç¦»çº¿&quot;,
 &quot;â connectingâ¦&quot;: &quot;â è¿æ¥ä¸­â¦&quot;,
 &quot;Paste&quot;: &quot;ç²è´´&quot;,
 &quot;Clipboard is empty.&quot;: &quot;åªè´´æ¿æ¯ç©ºçã&quot;,
 &quot;Pasted from clipboard.&quot;: &quot;å·²ä»åªè´´æ¿ç²è´´ã&quot;,
 &quot;Open the chat page first.&quot;: &quot;åæå¼èå¤©é¡µã&quot;,
 &quot;Type a message first.&quot;: &quot;åè¾å¥åå®¹ååéã&quot;,
 &quot;Backend connected.&quot;: &quot;å·²è¿ä¸åç«¯ã&quot;,
 &quot;Send failed. Is HTML\\BACKEND running?&quot;: &quot;åéå¤±è´¥ï¼åç«¯æ²¡å¼ï¼&quot;,
 &quot;Send failed&quot;: &quot;åéå¤±è´¥&quot;,
 &quot;Reloading messagesâ¦&quot;: &quot;æ­£å¨éæ°æåæ¶æ¯â¦&quot;,
 &quot;Settings saved&quot;: &quot;è®¾ç½®å·²ä¿å­&quot;,
 &quot;Could not save chatroom.json&quot;: &quot;chatroom.json ä¿å­å¤±è´¥&quot;,
 &quot;Select a player in Lexis â Online players, then come back.&quot;: &quot;åå¨ Lexisãå¨çº¿ç©å®¶ãééä¸ä¸ªç©å®¶ï¼ååæ¥ã&quot;,
 &quot;History Â· 3 messages&quot;: &quot;åå² Â· 3 æ¡æ¶æ¯&quot;,
 &quot;Nickname:&quot;: &quot;æµç§°ï¼&quot;,
 &quot;Reverie 0.4 Â· REVERIE&quot;: &quot;Reverie 0.4 Â· REVERIE&quot;,
 &quot;press INSERT to re-open&quot;: &quot;æ INSERT éæ°æå¼&quot;,
 &quot;Reverie&quot;: &quot;Reverie&quot;
};

&lt;/script&gt;
&lt;script&gt;
/* ============================================================================
   REVERIE UI Â· icons + widget builders
   Icons are SVG stand-ins for the FontAwesome 5 solid glyphs the lua uses
   (the original atlas font is part of GTA V and cannot be shipped here).
   ========================================================================== */

window.RV = window.RV || {};

(function () {
  &quot;use strict&quot;;

  var ICONS = {
    home:    &quot;M3 11.2 12 3l9 8.2V21h-6.4v-6.2h-5.2V21H3z&quot;,
    user:    &quot;M12 12.4a4.2 4.2 0 1 0 0-8.4 4.2 4.2 0 0 0 0 8.4ZM3.6 21c0-4.3 3.7-6.6 8.4-6.6s8.4 2.3 8.4 6.6z&quot;,
    users:   &quot;M9.2 12a3.6 3.6 0 1 0 0-7.2 3.6 3.6 0 0 0 0 7.2ZM1.8 20.6c0-3.6 3-5.6 7.4-5.6s7.4 2 7.4 5.6zM16.4 12.6a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM22.2 20.6c0-3-2.3-4.6-5.7-4.6 2.6 1 4.1 2.4 4.4 4.6z&quot;,
    car:     &quot;M3 14.4l1.9-5A2 2 0 0 1 6.8 8h10.4a2 2 0 0 1 1.9 1.4l1.9 5v4.6h-2.6v-1.6H5.6V19H3zM6.2 16.4a1.25 1.25 0 1 0 0-2.5 1.25 1.25 0 0 0 0 2.5zm11.6 0a1.25 1.25 0 1 0 0-2.5 1.25 1.25 0 0 0 0 2.5z&quot;,
    eye:     &quot;M12 5.2c5.3 0 9.4 3.9 10.7 6.8-1.3 2.9-5.4 6.8-10.7 6.8S2.6 14.9 1.3 12C2.6 9.1 6.7 5.2 12 5.2Zm0 2.2a4.6 4.6 0 1 0 0 9.2 4.6 4.6 0 0 0 0-9.2Z&quot;,
    cog:     &quot;M12 2.6l1.8 1 .3 2.1 1.9 1.1 2-.9 1.7 1.7-.9 2 1.1 1.9 2.1.3v2.4l-2.1.3-1.1 1.9.9 2-1.7 1.7-2-.9-1.9 1.1-.3 2.1h-2.4l-.3-2.1-1.9-1.1-2 .9-1.7-1.7.9-2L4.3 15l-2.1-.3v-2.4l2.1-.3 1.1-1.9-.9-2L6.2 6.4l2 .9 1.9-1.1.3-2.1zM12 8.6a3.4 3.4 0 1 0 0 6.8 3.4 3.4 0 0 0 0-6.8Z&quot;,
    close:   &quot;M6.2 6.2a1 1 0 0 1 1.4 0L12 10.6l4.4-4.4a1 1 0 1 1 1.4 1.4L13.4 12l4.4 4.4a1 1 0 0 1-1.4 1.4L12 13.4l-4.4 4.4a1 1 0 0 1-1.4-1.4l4.4-4.4-4.4-4.4a1 1 0 0 1 0-1.4Z&quot;,
    check:   &quot;M4.4 12.3 9.6 17.5 19.7 6.6l-1.9-1.7-8.2 8.9-3.4-3.4z&quot;,
    bolt:    &quot;M13.4 2 4.6 13.6h5.6L9.2 22l9.2-12h-5.7z&quot;,
    info:    &quot;M12 1.8A10.2 10.2 0 1 0 12 22.2 10.2 10.2 0 0 0 12 1.8Zm0 4a1.4 1.4 0 1 1 0 2.8 1.4 1.4 0 0 1 0-2.8Zm1.4 12.4h-2.8v-7h2.8z&quot;,
    warn:    &quot;M12 2.4 22.4 20.8H1.6zM11 8.2h2v6h-2zm0 7.6h2v2h-2z&quot;,
    star:    &quot;M12 2.3l2.9 6 6.6.9-4.8 4.6 1.2 6.6L12 17.3l-5.9 3.1 1.2-6.6L2.5 9.2l6.6-.9z&quot;,
    heart:   &quot;M12 21S2.6 14.7 2.6 8.9A5.2 5.2 0 0 1 12 5.6a5.2 5.2 0 0 1 9.4 3.3C21.4 14.7 12 21 12 21Z&quot;,
    trash:   &quot;M9 2.6h6l.8 1.8H20v2H4v-2h4.2zM5.6 7.8h12.8l-1 13.6H6.6zM9.4 10v9h1.8v-9zm3.4 0v9h1.8v-9z&quot;,
    plus:    &quot;M10.6 3.6h2.8v6.8h6.8v2.8h-6.8v6.8h-2.8v-6.8H3.8v-2.8h6.8z&quot;,
    power:   &quot;M12 2.4v9.2h0A1.4 1.4 0 0 1 10.6 10V2.4zM6.6 4.9 5 6.6a8.6 8.6 0 1 0 14 0l-1.6-1.7a7 7 0 1 1-10.8 0Z&quot;,
    wrench:  &quot;M20.6 3.4a5.8 5.8 0 0 0-7.5 7.1L3.6 20a1.6 1.6 0 0 0 2.3 2.3l9.5-9.5a5.8 5.8 0 0 0 7.1-7.5l-3.2 3.2-2.6-.7-.7-2.6z&quot;,
    down:    &quot;M4.9 9.1 12 16.2l7.1-7.1-1.7-1.7L12 12.8 6.6 7.4z&quot;,
    left:    &quot;M14.9 4.9 7.8 12l7.1 7.1 1.7-1.7L11.2 12l5.4-5.4z&quot;,
    globe:   &quot;M12 1.9A10.1 10.1 0 1 0 12 22.1 10.1 10.1 0 0 0 12 1.9Zm0 2c1.2 0 2.4 2.2 2.9 5.9h-5.8C9.6 6.1 10.8 3.9 12 3.9Zm-3.9 1c-.6 1.2-1 2.9-1.2 4.9H4.4a8.2 8.2 0 0 1 3.7-4.9Zm7.8 0a8.2 8.2 0 0 1 3.7 4.9h-2.5c-.2-2-.6-3.7-1.2-4.9ZM4.4 11.8h2.5c.2 2 .6 3.7 1.2 4.9a8.2 8.2 0 0 1-3.7-4.9Zm12.2 0h2.5a8.2 8.2 0 0 1-3.7 4.9c.6-1.2 1-2.9 1.2-4.9Zm-6.4 0h5.8c-.5 3.7-1.7 5.9-2.9 5.9s-2.4-2.2-2.9-5.9Z&quot;,
    clock:   &quot;M12 2.2A9.8 9.8 0 1 0 12 21.8 9.8 9.8 0 0 0 12 2.2Zm0 2a7.8 7.8 0 1 1 0 15.6 7.8 7.8 0 0 1 0-15.6Zm-.9 3.2v5.1l4 2.4 1-1.6-3.2-1.9V7.4z&quot;,
    save:    &quot;M3.4 3.4h13.4l4 4v13.2H3.4zM7 5.4v4.4h8.6V5.4zM6.4 13h11.2v6.6H6.4z&quot;,
    sliders: &quot;M3.4 6h8.2v2H3.4zm12.4 0h4.8v2h-4.8zM13.2 4.2a2.6 2.6 0 1 0 0 5.2 2.6 2.6 0 0 0 0-5.2ZM3.4 16h3.4v2H3.4zm7.6 0h9.6v2H11zM7.8 12.2a2.6 2.6 0 1 0 0 5.2 2.6 2.6 0 0 0 0-5.2Z&quot;,
    rocket:  &quot;M12 1.6c3.2 2 5 6.1 5 10.6l-2.4 2.3H9.4L7 12.2C7 7.7 8.8 3.6 12 1.6ZM9.6 16.4h4.8l-1.2 3.4h-2.4zM6.6 13.6 4 16.2l.4 3.4 2.6-2.6zm10.8 0 2.6 2.6-.4 3.4-2.6-2.6z&quot;,
    pointer: &quot;M5.6 2.6 20 12l-6.4 1 3.2 8-3.2 1.2-3.2-8-4.8 4.2z&quot;,
    skull:   &quot;M12 1.8c-5.2 0-8.4 3.4-8.4 8.2 0 2.8 1.2 4.8 3 6v3.4h3v2.8h4.8v-2.8h3v-3.4c1.8-1.2 3-3.2 3-6 0-4.8-3.2-8.2-8.4-8.2Zm-3.2 5.2a2 2 0 1 1 0 4 2 2 0 0 1 0-4Zm6.4 0a2 2 0 1 1 0 4 2 2 0 0 1 0-4ZM12 13.4l1.6 2.4h-3.2z&quot;,
    fire:    &quot;M12 1.8c.4 4 3.6 5.4 3.6 9 0 1.4-.6 2.4-1.6 2.8 2.6.6 4.6 2.6 4.6 5.2 0 .8-.2 1.6-.6 2.2H6c-1.6-1.2-2.6-3-2.6-5.2 0-3.2 2.4-5 3.6-7 1.4-2.4 2-4.6 2-7z&quot;,
    shield:  &quot;M12 1.8 21 5v7.4c0 5.2-3.8 8.8-9 10.8-5.2-2-9-5.6-9-10.8V5z&quot;,
    code:    &quot;M8.6 6.4 2 12l6.6 5.6 1.3-1.5L5 12l4.9-4.1zm6.8 0 1.3 1.5L21 12l-4.3 4.1 1.3 1.5L24 12z&quot;,
    comment: &quot;M3.4 3.4h17.2v13.4H12L6.6 21v-4.2H3.4z&quot;
  };

  function icon(name, cls) {
    var d = ICONS[name];
    if (!d) return null;
    var svg = document.createElementNS(&quot;http://www.w3.org/2000/svg&quot;, &quot;svg&quot;);
    svg.setAttribute(&quot;viewBox&quot;, &quot;0 0 24 24&quot;);
    svg.setAttribute(&quot;fill&quot;, &quot;currentColor&quot;);
    svg.setAttribute(&quot;aria-hidden&quot;, &quot;true&quot;);
    if (cls) svg.setAttribute(&quot;class&quot;, cls);
    var p = document.createElementNS(&quot;http://www.w3.org/2000/svg&quot;, &quot;path&quot;);
    p.setAttribute(&quot;d&quot;, d);
    svg.appendChild(p);
    return svg;
  }

  /* --- the lua format strings (&quot;%.0f m&quot;, &quot;%.2fx&quot;, &quot;%02.0f:00&quot;, &quot;%d%%&quot;) --- */
  function formatter(fmt) {
    if (!fmt) return function (v) { return String(Math.round(v)); };
    if (fmt === &quot;%02.0f:00&quot;) {
      return function (v) { return (v &lt; 10 ? &quot;0&quot; : &quot;&quot;) + Math.round(v) + &quot;:00&quot;; };
    }
    var m = fmt.match(/^%([0-9.]*)f(.*)$/);
    if (m) {
      var dec = m[1].charAt(m[1].length - 1) === &quot;.&quot; ? 0 : parseInt(m[1].split(&quot;.&quot;)[1] || &quot;0&quot;, 10);
      var suffix = m[2];
      return function (v) { return v.toFixed(dec) + suffix; };
    }
    m = fmt.match(/^%d(.*)$/);
    if (m) return function (v) { return String(Math.round(v)) + m[1]; };
    return function (v) { return String(v) + fmt; };
  }

  RV.icon = icon;
  RV.iconNames = Object.keys(ICONS);
  RV.formatter = formatter;
})();

&lt;/script&gt;
&lt;script&gt;
/* ============================================================================
   REVERIE UI Â· engine
   Replicates the layout / behaviour of Reverie.lua's menu shell:
   header 64 Â· sidebar 206 Â· footer 34 Â· window 820x630 Â· content pad 22.
   Everything here is a browser-side simulation: no natives, no network.
   ========================================================================== */

(function () {
  &quot;use strict&quot;;

  var PAGES = window.REVERIE_PAGES || [];
  var LISTS = window.REVERIE_LISTS || {};

  /* zh-CN dictionary from Reverie\lang\zh-CN.lua â same idea as reverie_tr() in the lua:
     the model keeps English source strings, the dictionary supplies the Chinese text. */
  var ZH = window.REVERIE_ZH || {};
  var ZH_NORM = {};
  Object.keys(ZH).forEach(function (k) { ZH_NORM[k.replace(/\\\\/g, &quot;\\&quot;)] = ZH[k]; });

  var ACCENTS = [
    { name: &quot;Indigo&quot;, rgb: [112, 98, 255] },
    { name: &quot;Cyan&quot;, rgb: [34, 211, 238] },
    { name: &quot;Emerald&quot;, rgb: [74, 222, 128] },
    { name: &quot;Amber&quot;, rgb: [251, 191, 36] },
    { name: &quot;Rose&quot;, rgb: [251, 113, 133] }
  ];

  var S = {
    tab: 0,
    scroll: 0,
    scrollTarget: 0,
    maxScroll: 0,
    accent: 0,
    rainbow: false,
    opacity: 75,
    zoom: 1,
    icons: true,
    toasts: true,
    debug: false,
    closed: false,
    openKey: &quot;INSERT&quot;,
    listening: null,
    tabSel: {},
    lang: &quot;zh&quot;,
    values: {}
  };

  function T(s) {
    if (S.lang !== &quot;zh&quot; || typeof s !== &quot;string&quot;) return s;
    return ZH[s] || ZH_NORM[s.replace(/\\\\/g, &quot;\\&quot;)] || s;
  }

  /* ------------------------------------------------------------------ dom */
  var win = document.getElementById(&quot;win&quot;);
  var stage = document.getElementById(&quot;stage&quot;);
  var hdr = document.getElementById(&quot;hdr&quot;);
  var tabsEl = document.getElementById(&quot;tabs&quot;);
  var view = document.getElementById(&quot;view&quot;);
  var paper = document.getElementById(&quot;paper&quot;);
  var scrollbar = document.getElementById(&quot;scrollbar&quot;);
  var toastsEl = document.getElementById(&quot;toasts&quot;);
  var hint = document.getElementById(&quot;hint&quot;);
  var debugEl = document.getElementById(&quot;debug&quot;);

  /* ----------------------------------------------------------------- utils */
  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function rgb(c, a) {
    return &quot;rgba(&quot; + c[0] + &quot;,&quot; + c[1] + &quot;,&quot; + c[2] + &quot;,&quot; + (a == null ? 1 : a) + &quot;)&quot;;
  }
  function setAccent(i) {
    S.accent = i;
    var c = ACCENTS[i % ACCENTS.length].rgb;
    document.documentElement.style.setProperty(&quot;--accent&quot;, c.join(&quot;, &quot;));
    S.rainbow = false;
    document.body.classList.remove(&quot;rainbow&quot;);
  }

  var FALLBACK_COLORS = LISTS.espPalette || [];

  /* ------------------------------------------------------------ toast ---- */
  function toast(desc, kind) {
    if (!S.toasts) return;
    var t = el(&quot;div&quot;, &quot;toast&quot; + (kind ? &quot; &quot; + kind : &quot;&quot;));
    var bar = el(&quot;div&quot;, &quot;bar&quot;);
    var tt = el(&quot;div&quot;, &quot;tt&quot;, &quot;Reverie&quot;);
    var td = el(&quot;div&quot;, &quot;td&quot;, desc);
    t.appendChild(bar); t.appendChild(tt); t.appendChild(td);
    toastsEl.appendChild(t);
    while (toastsEl.children.length &gt; 4) toastsEl.removeChild(toastsEl.firstChild);
    setTimeout(function () {
      t.classList.add(&quot;out&quot;);
      setTimeout(function () { if (t.parentNode) t.parentNode.removeChild(t); }, 220);
    }, 2600);
  }

  /* ------------------------------------------------------------- widgets -- */
  function sectionRow(r) {
    var d = el(&quot;div&quot;, &quot;section&quot;);
    var ic = RV.icon(r.icon);
    if (ic) d.appendChild(ic);
    d.appendChild(el(&quot;span&quot;, &quot;cap&quot;, T(r.label || &quot;&quot;)));
    d.appendChild(el(&quot;div&quot;, &quot;rule&quot;));
    return d;
  }

  function infoRow(r) {
    var d = el(&quot;div&quot;, &quot;row info plain&quot;);
    d.style.height = (r.h || 24) + &quot;px&quot;;
    d.appendChild(el(&quot;span&quot;, &quot;label&quot;, T(r.label || &quot;&quot;)));
    if (r.right) d.appendChild(el(&quot;span&quot;, &quot;right&quot;, T(r.right)));
    return d;
  }

  function itemRow(r) {
    var d = el(&quot;div&quot;, &quot;row item&quot;);
    d.style.height = (r.h || 26) + &quot;px&quot;;
    var ic = RV.icon(r.icon);
    if (ic) { ic.setAttribute(&quot;class&quot;, &quot;ic&quot;); d.appendChild(ic); }
    d.appendChild(el(&quot;span&quot;, &quot;label&quot;, T(r.label || &quot;&quot;)));
    if (r.right) d.appendChild(el(&quot;span&quot;, &quot;right&quot;, T(r.right)));
    return d;
  }

  function chatRow(r) {
    var d = el(&quot;div&quot;, &quot;row chat plain&quot; + (r.mine ? &quot; me&quot; : &quot;&quot;));
    d.style.height = (r.h || 21) + &quot;px&quot;;
    d.appendChild(el(&quot;span&quot;, &quot;t&quot;, r.time || &quot;--:--&quot;));
    d.appendChild(el(&quot;span&quot;, &quot;n&quot;, r.nick || &quot;?&quot;));
    d.appendChild(el(&quot;span&quot;, &quot;b&quot;, r.text || &quot;&quot;));
    return d;
  }

  function toggleRow(r) {
    var on = !!r.on;
    var d = el(&quot;div&quot;, &quot;row toggle&quot; + (r.desc ? &quot; has-desc&quot; : &quot;&quot;) + (on ? &quot; on&quot; : &quot;&quot;));
    d.style.height = (r.h || 46) + &quot;px&quot;;
    var lab = el(&quot;span&quot;, &quot;label&quot; + (r.desc ? &quot;&quot; : &quot; center&quot;), T(r.label || &quot;&quot;));
    d.appendChild(lab);
    if (r.desc) d.appendChild(el(&quot;span&quot;, &quot;desc&quot;, T(r.desc)));
    var tgl = el(&quot;span&quot;, &quot;tgl&quot;);
    var ck = RV.icon(&quot;check&quot;);
    if (ck) tgl.appendChild(ck);
    d.appendChild(tgl);
    d.addEventListener(&quot;click&quot;, function () {
      on = !on;
      r.on = on;
      d.classList.toggle(&quot;on&quot;, on);
      onToggleChange(r, on);
      if (S.toasts) toast((r.label || &quot;&quot;) + (on ? &quot; Â· on&quot; : &quot; Â· off&quot;), &quot;ok&quot;);
    });
    return d;
  }

  function sliderRow(r) {
    var v = typeof r.value === &quot;number&quot; ? r.value : r.min || 0;
    var fmt = RV.formatter(r.fmt);
    var d = el(&quot;div&quot;, &quot;row slider&quot;);
    d.style.height = (r.h || 44) + &quot;px&quot;;
    var lab = el(&quot;span&quot;, &quot;label&quot;, T(r.label || &quot;&quot;));
    var val = el(&quot;span&quot;, &quot;val&quot;, fmt(v));
    var track = el(&quot;div&quot;, &quot;track&quot;);
    var fill = el(&quot;div&quot;, &quot;fill&quot;);
    var knob = el(&quot;div&quot;, &quot;knob&quot;);
    track.appendChild(fill); track.appendChild(knob);
    d.appendChild(lab); d.appendChild(val); d.appendChild(track);

    function paint() {
      var ratio = (r.max &gt; r.min) ? (v - r.min) / (r.max - r.min) : 0;
      ratio = Math.max(0, Math.min(1, ratio));
      fill.style.width = (ratio * 100) + &quot;%&quot;;
      knob.style.left = (ratio * 100) + &quot;%&quot;;
      val.textContent = fmt(v);
    }
    paint();

    var dragging = false;
    function setFromEvent(e) {
      var rect = track.getBoundingClientRect();
      var ratio = (e.clientX - rect.left) / Math.max(1, rect.width);
      ratio = Math.max(0, Math.min(1, ratio));
      var raw = r.min + (r.max - r.min) * ratio;
      var step = r.step || 1;
      v = r.min + Math.round((raw - r.min) / step) * step;
      v = Math.max(r.min, Math.min(r.max, v));
      paint();
      r.value = v;
      onSliderChange(r, v);
    }
    d.addEventListener(&quot;pointerdown&quot;, function (e) {
      if (e.pointerType === &quot;touch&quot; &amp;&amp; !e.target.closest(&quot;.track&quot;)) return;
      d.setPointerCapture(e.pointerId);
      dragging = true;
      d.classList.add(&quot;drag&quot;);
      setFromEvent(e);
      e.preventDefault();
    });
    window.addEventListener(&quot;pointermove&quot;, function (e) { if (dragging) setFromEvent(e); });
    window.addEventListener(&quot;pointerup&quot;, function () {
      if (!dragging) return;
      dragging = false;
      d.classList.remove(&quot;drag&quot;);
    });
    return d;
  }

  function comboRow(r) {
    var idx = r.idx || 0;
    var d = el(&quot;div&quot;, &quot;row combo&quot;);
    d.style.height = (r.h || 42) + &quot;px&quot;;
    d.appendChild(el(&quot;span&quot;, &quot;label&quot;, T(r.label || &quot;&quot;)));
    var val = el(&quot;span&quot;, &quot;val&quot;, T((r.items &amp;&amp; r.items[idx]) || &quot;-&quot;));
    d.appendChild(val);
    var caret = RV.icon(&quot;down&quot;);
    if (caret) { caret.setAttribute(&quot;class&quot;, &quot;caret&quot;); d.appendChild(caret); }

    d.addEventListener(&quot;click&quot;, function (e) {
      e.stopPropagation();
      RV.openDropdown(d, { items: (r.items || []).map(T), idx: idx }, function (i) {
        idx = i;
        r.idx = i;
        val.textContent = T((r.items &amp;&amp; r.items[i]) || &quot;-&quot;);
        onComboChange(r, i);
      });
    });
    return d;
  }

  function buttonEl(label, iconName, style, h) {
    var b = el(&quot;button&quot;, &quot;btn&quot; + (style ? &quot; &quot; + style : &quot;&quot;));
    b.type = &quot;button&quot;;
    b.style.height = (h || 34) + &quot;px&quot;;
    var ic = RV.icon(iconName);
    if (ic) b.appendChild(ic);
    b.appendChild(el(&quot;span&quot;, null, T(label || &quot;&quot;)));
    b.addEventListener(&quot;click&quot;, function (e) {
      e.stopPropagation();
      onButton(r_label(b), style);
    });
    return b;
  }

  function r_label(b) {
    var span = b.querySelector(&quot;span&quot;);
    return span ? span.textContent : &quot;&quot;;
  }

  function onButton(label, style) {
    toast(label, style === &quot;danger&quot; ? &quot;err&quot; : &quot;ok&quot;);
  }

  function buttonRow(r) {
    var d = el(&quot;div&quot;, &quot;row plain&quot;);
    d.style.height = (r.h || 34) + &quot;px&quot;;
    var b = buttonEl(r.label, r.icon, r.style, r.h || 34);
    d.appendChild(b);
    return d;
  }

  function buttonsRow(r) {
    var d = el(&quot;div&quot;, &quot;row plain&quot;);
    d.style.height = (r.h || 34) + &quot;px&quot;;
    var row = el(&quot;div&quot;, &quot;btnrow&quot;);
    row.style.height = (r.h || 34) + &quot;px&quot;;
    (r.items || []).forEach(function (it) {
      var b = buttonEl(it.label, it.icon, it.style, r.h || 34);
      row.appendChild(b);
    });
    d.appendChild(row);
    return d;
  }

  function keybindRow(r) {
    var d = el(&quot;div&quot;, &quot;row keybind&quot;);
    d.style.height = (r.h || 42) + &quot;px&quot;;
    d.appendChild(el(&quot;span&quot;, &quot;label&quot;, T(r.label || &quot;&quot;)));
    var cap = el(&quot;span&quot;, &quot;keycap&quot;, r.key || &quot;INSERT&quot;);
    d.appendChild(cap);
    d.addEventListener(&quot;click&quot;, function () {
      S.listening = d;
      document.querySelectorAll(&quot;.row.keybind.listen&quot;).forEach(function (n) { n.classList.remove(&quot;listen&quot;); });
      d.classList.add(&quot;listen&quot;);
      cap.textContent = &quot;PRESS KEY&quot;;
    });
    return d;
  }

  function textboxRow(r) {
    var d = el(&quot;div&quot;, &quot;row textbox&quot;);
    d.style.height = (r.h || 36) + &quot;px&quot;;
    var lab = el(&quot;span&quot;, &quot;lab&quot;, T(r.label || &quot;&quot;));
    var input = el(&quot;input&quot;);
    input.type = &quot;text&quot;;
    input.value = r.value || &quot;&quot;;
    input.spellcheck = false;
    var uline = el(&quot;div&quot;, &quot;uline&quot;);
    d.appendChild(lab); d.appendChild(input); d.appendChild(uline);
    var labW = Math.max(30, (r.label || &quot;&quot;).length * 5.6 + 12);
    input.style.left = labW + &quot;px&quot;;
    input.style.width = &quot;calc(100% - &quot; + labW + &quot;px)&quot;;
    input.addEventListener(&quot;focus&quot;, function () { d.classList.add(&quot;focus&quot;); });
    input.addEventListener(&quot;blur&quot;, function () { d.classList.remove(&quot;focus&quot;); });
    input.addEventListener(&quot;mousedown&quot;, function (e) { e.stopPropagation(); });
    return d;
  }

  /* two/three fields sharing one list_row (clothing matrix, coordinates) */
  function fieldInput(label, w) {
    var wrap = el(&quot;div&quot;, &quot;field&quot;);
    if (label) wrap.appendChild(el(&quot;span&quot;, &quot;flab&quot;, label));
    var input = el(&quot;input&quot;);
    input.type = &quot;text&quot;;
    input.value = &quot;0&quot;;
    input.spellcheck = false;
    var uline = el(&quot;div&quot;, &quot;uline&quot;);
    wrap.appendChild(input);
    wrap.appendChild(uline);
    input.addEventListener(&quot;mousedown&quot;, function (e) { e.stopPropagation(); });
    input.addEventListener(&quot;focus&quot;, function () { wrap.classList.add(&quot;focus&quot;); });
    input.addEventListener(&quot;blur&quot;, function () { wrap.classList.remove(&quot;focus&quot;); });
    return wrap;
  }

  function flexRow(r) {
    var d = el(&quot;div&quot;, &quot;row plain flexbox&quot;);
    d.style.height = (r.h || 36) + &quot;px&quot;;
    (r.items || []).forEach(function (it) {
      var f = fieldInput(it.label);
      f.style.flex = &quot;1 1 0&quot;;
      d.appendChild(f);
    });
    return d;
  }

  function clothRow(r) {
    var names = r.items || [];
    var d = el(&quot;div&quot;, &quot;cloth&quot;);
    names.forEach(function (name, i) {
      var line = el(&quot;div&quot;, &quot;clothrow&quot;);
      line.style.height = (r.h || 22) + &quot;px&quot;;
      line.appendChild(el(&quot;span&quot;, &quot;nm&quot;, name));
      line.appendChild(fieldInput(&quot;&quot;));
      line.appendChild(fieldInput(&quot;&quot;));
      d.appendChild(line);
    });
    return d;
  }

  function coordsRow(r) {
    var d = el(&quot;div&quot;, &quot;row plain flexbox&quot;);
    d.style.height = (r.h || 34) + &quot;px&quot;;
    [&quot;X&quot;, &quot;Y&quot;, &quot;Z&quot;].forEach(function (lab) {
      var f = fieldInput(lab);
      f.style.flex = &quot;1 1 0&quot;;
      d.appendChild(f);
    });
    return d;
  }

  function heroRow() {    var d = el(&quot;div&quot;, &quot;hero&quot;);
    d.appendChild(el(&quot;div&quot;, &quot;n&quot;, &quot;Reverie&quot;));
    var sub = el(&quot;div&quot;, &quot;s&quot;, &quot;Reverie 0.4 Â· REVERIE&quot;);
    d.appendChild(sub);
    var badges = el(&quot;div&quot;, &quot;badges&quot;);
    [[&quot;a&quot;, &quot;bolt&quot;, &quot;2802&quot;], [&quot;b&quot;, &quot;star&quot;, &quot;lexis 1.0&quot;], [&quot;g&quot;, &quot;users&quot;, &quot;12 players&quot;]]
      .forEach(function (b) {
        var bd = el(&quot;div&quot;, &quot;badge &quot; + b[0]);
        var ic = RV.icon(b[1]);
        if (ic) bd.appendChild(ic);
        bd.appendChild(el(&quot;span&quot;, null, b[2]));
        badges.appendChild(bd);
      });
    d.appendChild(badges);
    return d;
  }

  function paletteRow(r) {
    var d = el(&quot;div&quot;, &quot;row pal plain&quot;);
    d.style.height = (r.h || 52) + &quot;px&quot;;
    d.appendChild(el(&quot;div&quot;, &quot;lab&quot;, T(r.label || &quot;&quot;)));
    var cells = el(&quot;div&quot;, &quot;cells&quot;);
    (r.colors || []).forEach(function (c, i) {
      var cell = el(&quot;div&quot;, &quot;cell&quot; + (i === (r.sel || 0) ? &quot; on&quot; : &quot;&quot;));
      cell.style.background = rgb(c, .92);
      cell.addEventListener(&quot;click&quot;, function () {
        cells.querySelectorAll(&quot;.cell&quot;).forEach(function (n) { n.classList.remove(&quot;on&quot;); });
        cell.classList.add(&quot;on&quot;);
      });
      cells.appendChild(cell);
    });
    d.appendChild(cells);
    return d;
  }

  /* ------------------------------------------------------------- pages -- */
  function buildTabs() {
    tabsEl.innerHTML = &quot;&quot;;
    PAGES.forEach(function (p, i) {
      var b = el(&quot;button&quot;, &quot;tab&quot; + (i === S.tab ? &quot; sel&quot; : &quot;&quot;));
      b.type = &quot;button&quot;;
      var ic = RV.icon(p.icon);
      if (ic) b.appendChild(ic);
      b.appendChild(el(&quot;span&quot;, null, T(p.name)));
      b.addEventListener(&quot;click&quot;, function () { selectTab(i); });
      tabsEl.appendChild(b);
    });
  }

  function selectTab(i) {
    S.tab = i;
    S.scroll = 0; S.scrollTarget = 0;
    RV.closeDropdown();
    Array.prototype.forEach.call(tabsEl.children, function (n, k) {
      n.classList.toggle(&quot;sel&quot;, k === i);
    });
    renderPage();
  }

  /* Heist payout tabs: one row of buttons + one visible row set at a time */
  function tabbarRow(r, container) {
    var d = el(&quot;div&quot;, &quot;row plain&quot;);
    d.style.height = (r.h || 34) + &quot;px&quot;;
    var row = el(&quot;div&quot;, &quot;btnrow&quot;);
    d.appendChild(row);
    var key = pageName() || &quot;page&quot;;
    var sel = S.tabSel[key] || 0;
    (r.items || []).forEach(function (it, i) {
      var b = el(&quot;button&quot;, &quot;btn&quot; + (i === sel ? &quot; accent&quot; : &quot;&quot;));
      b.type = &quot;button&quot;;
      b.style.height = (r.h || 34) + &quot;px&quot;;
      var ic = RV.icon(it.icon);
      if (ic) b.appendChild(ic);
      b.appendChild(el(&quot;span&quot;, null, it.label));
      b.addEventListener(&quot;click&quot;, function (e) {
        e.stopPropagation();
        S.tabSel[key] = i;
        Array.prototype.forEach.call(row.children, function (n, k) {
          n.classList.toggle(&quot;accent&quot;, k === i);
        });
        Array.prototype.forEach.call(container.querySelectorAll(&quot;.tabpage&quot;), function (p) {
          p.style.display = (parseInt(p.dataset.idx, 10) === i) ? &quot;&quot; : &quot;none&quot;;
        });
        measure();
      });
      row.appendChild(b);
    });
    return d;
  }

  function tabpageRow(r) {
    var key = pageName() || &quot;page&quot;;
    var sel = S.tabSel[key] || 0;
    var d = el(&quot;div&quot;, &quot;tabpage&quot;);
    d.dataset.idx = String(r.idx);
    d.style.display = (r.idx === sel) ? &quot;&quot; : &quot;none&quot;;
    renderRows(r.rows || [], d);
    return d;
  }

  function renderRows(rows, container) {
    rows.forEach(function (r) {
      var node = null;
      switch (r.t) {
        case &quot;section&quot;: node = sectionRow(r); break;
        case &quot;space&quot;: node = el(&quot;div&quot;); node.style.height = (r.h || 12) + &quot;px&quot;; break;
        case &quot;toggle&quot;: node = toggleRow(r); break;
        case &quot;slider&quot;: node = sliderRow(r); break;
        case &quot;combo&quot;: node = comboRow(r); break;
        case &quot;button&quot;: node = buttonRow(r); break;
        case &quot;buttons&quot;: node = buttonsRow(r); break;
        case &quot;keybind&quot;: node = keybindRow(r); break;
        case &quot;textbox&quot;: node = textboxRow(r); break;
        case &quot;info&quot;: node = infoRow(r); break;
        case &quot;row&quot;: node = itemRow(r); break;
        case &quot;chat&quot;: node = chatRow(r); break;
        case &quot;hero&quot;: node = heroRow(); break;
        case &quot;palette&quot;: node = paletteRow(r); break;
        case &quot;cloth&quot;: node = clothRow(r); break;
        case &quot;coords&quot;: node = coordsRow(r); break;
        case &quot;flexbox&quot;: node = flexRow(r); break;
        case &quot;tabbar&quot;: node = tabbarRow(r, container); break;
        case &quot;tabpage&quot;: node = tabpageRow(r); break;
        case &quot;two-col&quot;: node = twoCol(r); break;
        default: node = null;
      }
      if (!node) return;
      if (r.t !== &quot;section&quot; &amp;&amp; r.t !== &quot;space&quot;) node.style.marginBottom = &quot;4px&quot;;
      container.appendChild(node);
    });
  }

  function twoCol(r) {
    var d = el(&quot;div&quot;, &quot;twocol&quot;);
    var left = el(&quot;div&quot;, &quot;col&quot;);
    var right = el(&quot;div&quot;, &quot;col&quot;);
    renderRows(r.left || [], left);
    renderRows(r.right || [], right);
    var div = el(&quot;div&quot;, &quot;divider&quot;);
    d.appendChild(left); d.appendChild(div); d.appendChild(right);
    setTimeout(function () {
      div.style.height = Math.max(left.offsetHeight, right.offsetHeight) + &quot;px&quot;;
    }, 0);
    return d;
  }

  function renderPage() {
    var p = PAGES[S.tab];
    if (!p) return;
    paper.innerHTML = &quot;&quot;;
    paper.scrollTop = 0;
    paper.appendChild(el(&quot;div&quot;, &quot;page-title&quot;, T(p.title || p.name)));
    if (p.desc) paper.appendChild(el(&quot;div&quot;, &quot;page-desc&quot;, T(p.desc)));
    var line = el(&quot;div&quot;, &quot;page-line&quot;);
    paper.appendChild(line);
    var rows = el(&quot;div&quot;, &quot;rows&quot;);
    renderRows(prepareRows(p.name, p.rows || []), rows);
    paper.appendChild(rows);
    measure();
    paper.style.transform = &quot;translateY(0px)&quot;;
    S.scroll = 0; S.scrollTarget = 0;
    updateScrollbar();
  }

  function measure() {
    var h = paper.offsetHeight + 20; /* bottom padding */
    S.maxScroll = Math.max(0, h - view.clientHeight);
  }

  function updateScrollbar() {
    if (S.maxScroll &lt;= 1) { scrollbar.style.opacity = 0; return; }
    var vh = view.clientHeight - 16;
    var th = Math.max(28, vh * (view.clientHeight / (view.clientHeight + S.maxScroll)));
    var ry = S.scroll / S.maxScroll;
    scrollbar.style.height = th + &quot;px&quot;;
    scrollbar.style.top = (8 + ry * (vh - th)) + &quot;px&quot;;
    scrollbar.style.opacity = 1;
  }

  function tick() {
    S.scroll += (S.scrollTarget - S.scroll) * 0.28;
    if (Math.abs(S.scrollTarget - S.scroll) &lt; 0.4) S.scroll = S.scrollTarget;
    paper.style.transform = &quot;translateY(&quot; + (-S.scroll).toFixed(2) + &quot;px)&quot;;
    updateScrollbar();
    requestAnimationFrame(tick);
  }

  view.addEventListener(&quot;wheel&quot;, function (e) {
    e.preventDefault();
    var before = S.scrollTarget;
    S.scrollTarget = Math.max(0, Math.min(S.maxScroll, S.scrollTarget + e.deltaY));
    if (before === S.scrollTarget) scrollOuter(e.deltaY);
  }, { passive: false });

  /* --------------------------------------------------------- dropdown ---- */
  var ddEl = null;
  RV.openDropdown = function (anchor, row, onPick) {
    RV.closeDropdown();
    var d = el(&quot;div&quot;, &quot;dropdown&quot;);
    (row.items || []).forEach(function (item, i) {
      var it = el(&quot;div&quot;, &quot;dd-item&quot; + (i === (row.idx || 0) ? &quot; sel&quot; : &quot;&quot;), item);
      it.addEventListener(&quot;click&quot;, function (e) {
        e.stopPropagation();
        row.idx = i;
        onPick(i);
        RV.closeDropdown();
      });
      d.appendChild(it);
    });
    var wr = win.getBoundingClientRect();
    var ar = anchor.getBoundingClientRect();
    var sc = wr.width / win.offsetWidth || 1;
    var left = (ar.left - wr.left) / sc;
    var top = (ar.bottom - wr.top) / sc + 6;
    d.style.left = left + &quot;px&quot;;
    d.style.width = (ar.width / sc) + &quot;px&quot;;
    d.style.top = top + &quot;px&quot;;
    if (top + 280 &gt; wr.height / sc) {
      d.style.top = Math.max(8, (ar.top - wr.top) / sc - 6 - Math.min(280, 29 * (row.items || []).length + 8)) + &quot;px&quot;;
    }
    win.appendChild(d);
    ddEl = d;
  };
  RV.closeDropdown = function () {
    if (ddEl &amp;&amp; ddEl.parentNode) ddEl.parentNode.removeChild(ddEl);
    ddEl = null;
  };
  document.addEventListener(&quot;mousedown&quot;, function (e) {
    if (ddEl &amp;&amp; !ddEl.contains(e.target)) RV.closeDropdown();
  });

  /* ------------------------------------------------------ settings hooks -- */
  function pageName() { return (PAGES[S.tab] || {}).name; }

  function onComboChange(row, idx) {
    if (pageName() !== &quot;Settings&quot;) return;
    if (row.label === &quot;Colour&quot;) {
      S.accent = idx;
      setAccent(idx);
      toast(T(&quot;Accent&quot;) + &quot; Â· &quot; + T(ACCENTS[idx].name), &quot;ok&quot;);
    } else if (row.label === &quot;Language&quot;) {
      applyLang(idx === 1 ? &quot;zh&quot; : &quot;en&quot;);
    }
  }

  /* è¯­è¨æé®è´´çé®å¸½å·¦ä¾§æï¼é®ä½æ¹ååé¿ä¹ä¸ä¼æä¸ */
  function placeLangBtn() {
    var hk = document.getElementById(&quot;hdrKey&quot;);
    var lb = document.getElementById(&quot;langBtn&quot;);
    if (!hk || !lb) return;
    var w = hk.offsetWidth || 55;
    lb.style.right = (54 + w + 8) + &quot;px&quot;;
  }

  function applyChrome() {
    var hdrSub = document.getElementById(&quot;hdrSub&quot;);
    var footLeft = document.getElementById(&quot;footLeft&quot;);
    if (hdrSub) hdrSub.textContent = T(&quot;reverie v0.4&quot;);
    if (footLeft) footLeft.textContent = T(&quot;click Â· drag header Â· wheel scroll&quot;);
    if (hint) hint.textContent = T(&quot;press INSERT to re-open&quot;);
    var cap = document.getElementById(&quot;acctCap&quot;);
    if (cap) cap.textContent = &quot;ACCOUNT&quot;;
    var lb = document.getElementById(&quot;langBtn&quot;);
    if (lb) {
      lb.title = S.lang === &quot;zh&quot; ? &quot;Switch language Â· åæ¢å°è±æ&quot; : &quot;Switch language Â· åæ¢å°ä¸­æ&quot;;
      Array.prototype.forEach.call(lb.children, function (n) {
        n.classList.toggle(&quot;on&quot;, n.dataset.lang === S.lang);
      });
      placeLangBtn();
    }
  }

  function applyLang(next) {
    S.lang = next;
    document.documentElement.setAttribute(&quot;lang&quot;, next === &quot;zh&quot; ? &quot;zh-CN&quot; : &quot;en&quot;);
    buildTabs();
    renderPage();
    applyChrome();
    toast(next === &quot;zh&quot; ? &quot;çé¢è¯­è¨ï¼ä¸­æ&quot; : &quot;Interface language: English&quot;, &quot;ok&quot;);
  }

  function onSliderChange(row, v) {
    if (pageName() !== &quot;Settings&quot;) return;
    if (row.label === &quot;Window opacity&quot;) {
      S.opacity = v;
      win.style.setProperty(&quot;--opacity&quot;, (v / 100).toFixed(2));
      document.documentElement.style.setProperty(&quot;--opacity&quot;, (v / 100).toFixed(2));
    } else if (row.label === &quot;UI scale&quot;) {
      S.zoom = v / 100;
      document.documentElement.style.setProperty(&quot;--zoom&quot;, S.zoom.toFixed(2));
    }
  }

  function onToggleChange(row, on) {
    if (pageName() !== &quot;Settings&quot;) return;
    if (row.label === &quot;Toast notifications&quot;) S.toasts = on;
    else if (row.label === &quot;Font Awesome icons&quot;) {
      S.icons = on;
      document.body.classList.toggle(&quot;no-icons&quot;, !on);
    } else if (row.label === &quot;Debug overlay&quot;) {
      S.debug = on;
      document.body.classList.toggle(&quot;debug-on&quot;, on);
    } else if (row.label === &quot;Rainbow accent&quot;) {
      S.rainbow = on;
      document.body.classList.toggle(&quot;rainbow&quot;, on);
    }
  }

  /* è®¾ç½®é¡µçè¡è¦åæ å½åå¤å£³ç¶æï¼åé¡µåæ¥ä¸è½åå°é»è®¤å¼ï¼ */
  function prepareRows(name, rows) {
    if (name !== &quot;Settings&quot;) return rows;
    rows.forEach(function (r) {
      if (r.t === &quot;toggle&quot;) {
        if (r.label === &quot;Toast notifications&quot;) r.on = S.toasts;
        else if (r.label === &quot;Font Awesome icons&quot;) r.on = S.icons;
        else if (r.label === &quot;Debug overlay&quot;) r.on = S.debug;
        else if (r.label === &quot;Rainbow accent&quot;) r.on = S.rainbow;
      } else if (r.t === &quot;slider&quot;) {
        if (r.label === &quot;Window opacity&quot;) r.value = Math.round(S.opacity);
        else if (r.label === &quot;UI scale&quot;) r.value = Math.round(S.zoom * 100);
      } else if (r.t === &quot;combo&quot;) {
        if (r.label === &quot;Colour&quot;) r.idx = S.accent;
        else if (r.label === &quot;Language&quot;) r.idx = S.lang === &quot;zh&quot; ? 1 : 0;
      }
    });
    return rows;
  }

  /* --------------------------------------------------------------- shell -- */
  function fit() {
    var f = window.innerWidth &lt;= 650 ? 1 : Math.min((window.innerWidth - 40) / 820, (window.innerHeight - 128) / 630, 1);
    document.documentElement.style.setProperty(&quot;--fit&quot;, f.toFixed(3));
  }
  window.addEventListener(&quot;resize&quot;, fit);

  function setClosed(v) {
    S.closed = v;
    win.classList.toggle(&quot;closed&quot;, v);
    document.body.classList.toggle(&quot;win-closed&quot;, v);
    if (v) RV.closeDropdown();
  }

  /* window drag */
  (function () {
    var drag = null;
    hdr.addEventListener(&quot;mousedown&quot;, function (e) {
      if (e.target.closest(&quot;.close&quot;) || e.target.closest(&quot;.langbtn&quot;)) return;
      var wr = win.getBoundingClientRect();
      drag = { x: e.clientX, y: e.clientY, left: parseFloat(win.dataset.ox || &quot;0&quot;), top: parseFloat(win.dataset.oy || &quot;0&quot;) };
      e.preventDefault();
    });
    window.addEventListener(&quot;mousemove&quot;, function (e) {
      if (!drag) return;
      var sc = win.getBoundingClientRect().width / win.offsetWidth || 1;
      var dx = (e.clientX - drag.x) / sc;
      var dy = (e.clientY - drag.y) / sc;
      win.style.transform = &quot;translate(&quot; + dx + &quot;px,&quot; + dy + &quot;px)&quot;;
    });
    window.addEventListener(&quot;mouseup&quot;, function () { drag = null; });
  })();

  document.getElementById(&quot;close&quot;).addEventListener(&quot;click&quot;, function () { setClosed(true); });

  /* é¡¶æ è¯­è¨æé®ï¼ä¸é®ä¸­è±åæ¢ï¼å è®¾ç½® â Language ä¸ææ¯åä¸ä¸ªç¶æï¼ */
  var langBtnEl = document.getElementById(&quot;langBtn&quot;);
  if (langBtnEl) {
    langBtnEl.addEventListener(&quot;mousedown&quot;, function (e) { e.stopPropagation(); });
    langBtnEl.addEventListener(&quot;click&quot;, function (e) {
      e.stopPropagation();
      applyLang(S.lang === &quot;zh&quot; ? &quot;en&quot; : &quot;zh&quot;);
    });
  }

  document.addEventListener(&quot;keydown&quot;, function (e) {
    if (e.key === &quot;Insert&quot;) {
      setClosed(!S.closed);
      return;
    }
    if (e.key === &quot;Escape&quot;) { RV.closeDropdown(); return; }
    if (S.listening) {
      var names = {
        &quot; &quot;: &quot;SPACE&quot;, ArrowUp: &quot;UP&quot;, ArrowDown: &quot;DOWN&quot;, ArrowLeft: &quot;LEFT&quot;, ArrowRight: &quot;RIGHT&quot;,
        Control: &quot;CTRL&quot;, Shift: &quot;SHIFT&quot;, Alt: &quot;ALT&quot;, Escape: &quot;ESC&quot;
      };
      var name = names[e.key] || (e.key.length === 1 ? e.key.toUpperCase() : e.key.toUpperCase());
      var cap = S.listening.querySelector(&quot;.keycap&quot;);
      if (cap) cap.textContent = name;
      if (S.listening.querySelector(&quot;.label&quot;) &amp;&amp; S.listening.querySelector(&quot;.label&quot;).textContent === &quot;Menu key&quot;) {
        S.openKey = name;
        var hk = document.getElementById(&quot;hdrKey&quot;);
        if (hk) { hk.textContent = name; placeLangBtn(); }
      }
      S.listening.classList.remove(&quot;listen&quot;);
      S.listening = null;
      e.preventDefault();
    }
  });

  function setScroll(value) {
    S.scrollTarget = Math.max(0, Math.min(S.maxScroll, value));
  }

  function scrollOuter(delta) {
    window.parent.postMessage({ type: 'reverie-preview:scroll', delta: delta }, '*');
  }

  hint.addEventListener('click', function () { setClosed(false); });

  var touchY = null;
  view.addEventListener('touchstart', function (event) {
    if (event.touches.length !== 1 || event.target.closest('input, .track')) return;
    touchY = event.touches[0].clientY;
  }, { passive: true });
  view.addEventListener('touchmove', function (event) {
    if (touchY === null || event.touches.length !== 1) return;
    var nextY = event.touches[0].clientY;
    var delta = touchY - nextY;
    touchY = nextY;
    var before = S.scrollTarget;
    var scale = win.getBoundingClientRect().width / win.offsetWidth;
    setScroll(S.scrollTarget + delta / scale);
    if (before === S.scrollTarget) scrollOuter(delta);
    event.preventDefault();
  }, { passive: false });
  view.addEventListener('touchend', function () { touchY = null; });

  function reportHeight() {
    var height = Math.ceil(win.getBoundingClientRect().height);
    window.parent.postMessage({ type: 'reverie-preview:height', height: height }, '*');
  }
  window.addEventListener('message', function (event) {
    if (event.source !== window.parent || event.data?.type !== 'reverie-preview:measure') return;
    requestAnimationFrame(reportHeight);
  });
  if (typeof ResizeObserver !== 'undefined') {
    new ResizeObserver(reportHeight).observe(win);
  }
  window.addEventListener('resize', reportHeight);
  requestAnimationFrame(reportHeight);

  /* ---------------------------------------------------------------- boot -- */
  function boot() {
    fit();
    document.documentElement.style.setProperty(&quot;--opacity&quot;, &quot;0.75&quot;);

    /* åç settings.lang = &quot;auto&quot;ï¼è·éç³»ç»è¯­è¨ */
    S.lang = &quot;zh&quot;;
    document.documentElement.setAttribute(&quot;lang&quot;, S.lang === &quot;zh&quot; ? &quot;zh-CN&quot; : &quot;en&quot;);

    buildTabs();
    renderPage();
    applyChrome();
    tick();
    setClosed(false);

    debugEl.textContent =
      &quot;REVERIE UI Â· replica\npage: &quot; + &quot;\nindex: 0.4\nscale: 1.00&quot;;

    setInterval(function () {
      if (!S.debug) return;
      var p = PAGES[S.tab] || {};
      debugEl.textContent =
        &quot;REVERIE UI Â· replica\npage: &quot; + (p.name || &quot;-&quot;) +
        &quot;\nscroll: &quot; + S.scroll.toFixed(1) + &quot; / &quot; + S.maxScroll.toFixed(0) +
        &quot;\naccent: &quot; + ACCENTS[S.accent].name;
    }, 400);

    /* Settings rows that drive the shell are wired through labels above. */
  }

  boot();
  requestAnimationFrame(reportHeight);
})();

&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
" style="height:630px" title="Reverie Lua äº¤äºå¼åè½é¢è§"></iframe></section>
<h2 class="anchor anchorTargetStickyNavbar_Vzrq" id="demo"><strong>é¨ååè½å±ç¤º</strong><a aria-label="demoçç´æ¥é¾æ¥" class="hash-link" href="#demo" title="demoçç´æ¥é¾æ¥" translate="no">â</a></h2>
<figure><img alt="Reverie å è½½çé¢" decoding="async" height="949" loading="lazy" src="https://pic1.imgdb.cn/i/034sqFelbYUSdVg4rpdys6.webp" style="width:100%;height:auto" width="1280"/></figure>
<figure><img alt="Reverie ä¸åå½å®æ¼ç¤º" decoding="async" height="781" loading="lazy" src="https://pic1.imgdb.cn/i/034sqFnmqk1LCZlcDTN89z.webp" style="width:100%;height:auto" width="1536"/></figure>
<figure><img alt="Reverie ä¸»é¢èæ¯ä¸ ESP å±ç¤º" decoding="async" height="894" loading="lazy" src="https://pic1.imgdb.cn/i/034sqFuQVc2aL7foZ7Hg15.webp" style="width:100%;height:auto" width="1536"/></figure>
<figure><img alt="Reverie ä¿éä¸è½¦éæ¼ç¤º" decoding="async" height="885" loading="lazy" src="https://pic1.imgdb.cn/i/034sqG2WEnL4UM6mdlyzfw.webp" style="width:100%;height:auto" width="1536"/></figure>
<figure><img alt="Reverie èå¤©å®¤å±ç¤º" decoding="async" height="883" loading="lazy" src="https://pic1.imgdb.cn/i/034sqG8y6TRulfywNXm6hm.webp" style="width:100%;height:auto" width="1148"/></figure></div></article>
#!/bin/bash

FILENAME="payload_<span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo stretchy="false">(</mo><mi>d</mi><mi>a</mi><mi>t</mi><mi>e</mi><mo>+</mo><mi>e</mi><mi>c</mi><mi>h</mi><mi>o</mi><mi mathvariant="normal">&quot;</mi><mi>T</mi><mi>h</mi><mi>i</mi><mi>s</mi><mi>i</mi><mi>s</mi><mi>a</mi><mi>h</mi><mi>e</mi><mi>a</mi><mi>r</mi><mi>t</mi><mi>b</mi><mi>e</mi><mi>a</mi><mi>t</mi><mi>c</mi><mi>o</mi><mi>m</mi><mi>m</mi><mi>i</mi><mi>t</mi><mi>o</mi><mi>n</mi></mrow><annotation encoding="application/x-tex">(date +%Y%m%d%H%M%S).txt&quot;
echo &quot;This is a heartbeat commit on</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span class="mord mathnormal">d</span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">+</span><span class="mspace" style="margin-right:0.2222em;"></span></span><span class="base"><span class="strut" style="height:0.6944em;"></span><span class="mord mathnormal">ec</span><span class="mord mathnormal">h</span><span class="mord mathnormal">o</span><span class="mord">&quot;</span><span class="mord mathnormal" style="margin-right:0.13889em;">T</span><span class="mord mathnormal">hi</span><span class="mord mathnormal">s</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord mathnormal">ah</span><span class="mord mathnormal">e</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">t</span><span class="mord mathnormal">b</span><span class="mord mathnormal">e</span><span class="mord mathnormal">a</span><span class="mord mathnormal">t</span><span class="mord mathnormal">co</span><span class="mord mathnormal">mmi</span><span class="mord mathnormal">t</span><span class="mord mathnormal">o</span><span class="mord mathnormal">n</span></span></span></span>(date)" > <span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>F</mi><mi>I</mi><mi>L</mi><mi>E</mi><mi>N</mi><mi>A</mi><mi>M</mi><mi>E</mi><mi>e</mi><mi>c</mi><mi>h</mi><mi>o</mi><mi mathvariant="normal">&quot;</mi><mi>A</mi><mi>d</mi><mi>d</mi><mi>i</mi><mi>n</mi><mi>g</mi><mi>s</mi><mi>o</mi><mi>m</mi><mi>e</mi><mi>r</mi><mi>a</mi><mi>n</mi><mi>d</mi><mi>o</mi><mi>m</mi><mi>c</mi><mi>o</mi><mi>n</mi><mi>t</mi><mi>e</mi><mi>n</mi><mi>t</mi><mo>:</mo><mi mathvariant="normal">&quot;</mi><mo>&gt;</mo><mo>&gt;</mo></mrow><annotation encoding="application/x-tex">FILENAME
echo &quot;Adding some random content:&quot; &gt;&gt;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="mord mathnormal" style="margin-right:0.13889em;">F</span><span class="mord mathnormal" style="margin-right:0.07847em;">I</span><span class="mord mathnormal">L</span><span class="mord mathnormal" style="margin-right:0.10903em;">EN</span><span class="mord mathnormal">A</span><span class="mord mathnormal" style="margin-right:0.05764em;">ME</span><span class="mord mathnormal">ec</span><span class="mord mathnormal">h</span><span class="mord mathnormal">o</span><span class="mord">&quot;</span><span class="mord mathnormal">A</span><span class="mord mathnormal">dd</span><span class="mord mathnormal">in</span><span class="mord mathnormal" style="margin-right:0.03588em;">g</span><span class="mord mathnormal">so</span><span class="mord mathnormal">m</span><span class="mord mathnormal" style="margin-right:0.02778em;">er</span><span class="mord mathnormal">an</span><span class="mord mathnormal">d</span><span class="mord mathnormal">o</span><span class="mord mathnormal">m</span><span class="mord mathnormal">co</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">:</span><span class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut" style="height:0.7335em;vertical-align:-0.0391em;"></span><span class="mord">&quot;</span><span class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&gt;&gt;</span></span></span></span>FILENAME
head /dev/urandom | tr -dc A-Za-z0-9 | head -c 512 >> $FILENAME

git add $FILENAME

git commit -m "Beat on $(date)"

git push origin main

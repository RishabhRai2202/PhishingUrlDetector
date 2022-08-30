dot = 0
legitimate = 1
URL = input(&quot;ENTER THE URL:- &quot;)
# print(URL)
# CONDITION 1 LENGTH
if not URL.find(&quot;http&quot;):
length = len(URL)
if length &lt; 54:
legitimate = legitimate + 1
elif 54 &lt;= length &lt;= 75:
print(&quot;URL LENGTH IS SUSPICIOUS&quot;)
else:
print(&quot;PHISHING URL&quot;)
# CONDITION 2 TINY and BIT
if URL.find(&quot;bit.ly&quot;) &gt; 0:
print(&quot;URL CONTAINS bit.ly (suspicious)&quot;)

elif URL.find(&quot;tinyurl&quot;) &gt; 0:
print(&quot;URL CONTAINS tinyurl (suspicious)&quot;)
else:
legitimate = legitimate + 1
# CONDITION 3 @ SYMBOL
if URL.find(&quot;@&quot;) &gt; 0:
print(&quot;PHISHING URL (contains @)&quot;)
else:
legitimate = legitimate + 1
# CONDITION 4 -
if URL.find(&quot;-&quot;) &gt; 0:
print(&quot;PHISHING URL (contains -)&quot;)
else:
legitimate = legitimate + 1
# CONDITION 5 // &gt;7 position
if URL[7:].find(&quot;//&quot;) &gt;= 7:
print(&quot;PHISHING URL (contains //)&quot;)
else:
legitimate = legitimate + 1
# CONDITION 6 http
if URL.find(&quot;https&quot;):
print(&quot;URL CONTAINS http (suspicious)&quot;)
else:
legitimate = legitimate + 1
# CONDITION 7 dotted
url_list = list(URL)
for i in range(0, length):
if url_list[i] == &#39;.&#39;:
dot = dot + 1
if URL.find(&quot;www&quot;) &gt; 0:
if 2 &lt;= dot &lt;= 3:
legitimate = legitimate + 1
else:
print(&quot;PHISHING URL&quot;)
else:
# CONDITION 8
# print(URL[8:])
# URL[8:URL[8:].find(&quot;/&quot;)]
if 1 &lt;= dot &lt;= 2:
legitimate = legitimate + 1
elif dot == 3:
if (URL[8:].find(&quot;/&quot;)) &gt; 0:
final_url_ip = list(URL[8:(URL[8:].find(&quot;/&quot;))])
final_length = len(URL[8:(URL[8:].find(&quot;/&quot;))])
else:
final_url_ip = list(URL[8:])
final_length = len(URL[8:])
for i in range(0, final_length):
if 48 &lt;= ord(final_url_ip[i]) &lt;= 57 or ord(final_url_ip[i])
== 46:
continue
else:
break
if i + 1 == final_length:
legitimate = legitimate + 1
else:
print(&quot;PHISHING !!!!&quot;)
else:

print(&quot;PHISHING URL&quot;)
# CONDITION 8
# print(URL[8:])
# URL[8:URL[8:].find(&quot;/&quot;)]
if legitimate == 8:
print(&quot;SITE IS LEGITIMATE.&quot;)
else:
print(&quot;AT LEAST INPUT A URL BROOOOOOOO!!!!&quot;)

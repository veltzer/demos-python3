This is ${foo}
Copyright Linus Torvalds ${years(2007)}

% for a in range(10):
	${a}
% endfor

<%
	import platform # for node
	hostname=platform.node()
%>

You are running on ${hostname}

% if 'a' in d:
	${d['a']}
	'a' is in d
% else:
	'a' is not in d
% endif

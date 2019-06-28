import robotparser

rp = robotparser.RobotFileParser('http://blog.daum.net/robots.txt')
rp.read()
rp.can_fetch('mycrawler','http://blog.daum.net')
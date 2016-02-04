from fabric.api import local

def test():
	local("cp /home/Ashish/Scripts/index.html /tmp/fabric-test/index.html")
	local("cd /tmp/fabric-test && touch file1 file2 file3")

def commit():
	local("cd /tmp/fabric-test && git add . && git commit -m test")

def push():
	local("cd /tmp/fabric-test && git push origin master")

def prepare_deploy():
	test()
	commit()
	push()

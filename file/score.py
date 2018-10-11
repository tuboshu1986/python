class Score():
	"****"
	def __init__(self):
		self.scores = [];
		self.scoreNames = [];
		
	def level1(self, s):
		"计算并缓存"
		name = self.level(s);
		self.scores.append(s);
		self.scoreNames.append(name);
		return name;

		
	def level(self, s):
		"****"
		msg = "";
		if s < 60 :
			msg = "F";
		elif 70 > s >= 60:
			msg = "E";
		elif 80 > s >= 70:
			msg = "D";
		elif 90 > s >= 80:
			msg = "C";
		elif 100 > s >= 90:
			msg = "B";
		else:
			msg = "A";

		return msg;
		
	def avg(self):
		sum = 0;
		for s in self.scores:
			sum += s;
		return sum / len(self.scores);
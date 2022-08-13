run:
	@pip install numpy
	@pip install pandas
	@pip install pickle-mixin
	@pip install matplotlib
	@pip install gensim
	@echo "Q1 done"
	@cd ./Q2 && python3 Preprocesssing.py
	@echo "Q2 Preprocessing Done"
	@cd ./Q3 && python3 Q3.py && python3 Q3_D.py
	@echo "Q3 done"

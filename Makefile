thrift:
	rm -rf gen_py && mkdir gen_py
	thrift-0.18.1 --gen py --out gen_py tutorial.thrift

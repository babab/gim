BASE_PATH		= /usr
BIN_PATH		= ${BASE_PATH}/local/bin

make:
	@echo 'make install   -- install gim'
	@echo 'make uninstall -- uninstall gim'

install:
	install -Dm 755 gim ${BIN_PATH}
uninstall:
	rm -f $(BIN_PATH)/gim

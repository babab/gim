BASE_PATH		= /usr
BIN_PATH		= ${BASE_PATH}/local/bin

make:
	@echo 'make install   -- install gim'
	@echo 'make uninstall -- uninstall gim'

install:
	install -Dm 755 gim ${BIN_PATH}
	ln -sf ${BIN_PATH}/gim ${BIN_PATH}/git-edit
uninstall:
	rm -f $(BIN_PATH)/gim
	rm -f $(BIN_PATH)/git-edit

CFLAGS = -Wall -pthread -DGLEW_STATIC -DWIN32 -std=c++2a -O3 -Wextra
COMPILER = g++
LIBRARY = -Bstatic -lglew32 -lglfw3 -lopengl32
INCLUDEDIRS = -I./include
FORMAT = exe
EXEC = source
OUT = a

ifdef $(DEBUG)
	CFLAGS += -DDEBUG
endif

all: src/$(EXEC).cpp
	@echo cond
	@echo Making directories...
	mkdir -p bin

	$(COMPILER) -c -o bin/$(EXEC).o $(CFLAGS) src/$(EXEC).cpp $(INCLUDEDIRS)
	$(COMPILER) -o bin/$(OUT).$(FORMAT) bin/$(EXEC).o $(LIBRARY)

	@echo Done.


run:
	./bin/$(OUT).$(FORMAT)

debug:

clean:
	rm -Rfv *.exe *.o
	rm -Rfv bin
# Install GO on your automation setup

Go is an open source programming language.  

Some of the tools we are using in this repository require GO to be installed:

- The command line tool gRPCurl
- The gNMI client gnmi

Here's the instructions to install GO on your automation setup:

- Install GO

```bash
uname -m
wget https://dl.google.com/go/go1.18.3.linux-amd64.tar.gz
sudo tar -C /usr/local/ -xzf go1.18.3.linux-amd64.tar.gz
ls /usr/local/
```

- Set the GOROOT and GOPATH environment variables

```bash
echo $HOME
echo $PATH
echo $GOROOT
echo $GOPATH
export GOROOT=/usr/local/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$GOROOT/bin:$PATH
echo $PATH
```

- Verify

```bash
go env | grep 'GOROOT\|GOPATH'
go version
which go
```

That's it.

- Never used GO?

If you never used GO, you may want to run your first program

```bash
package main
import "fmt"
func main() {
    fmt.Println("I love CVP")
}
```

Copy the above code in the file test.go and use go run command

```bash
go run test.go
```

Use the go build command to build a binary

```bash
go build test.go
```

You can then execute the binary directly

```bash
ls $GOPATH/bin/
```

```bash
test
```

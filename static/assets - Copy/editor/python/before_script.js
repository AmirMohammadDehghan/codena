

// output functions are configurable.  This one just appends some text
// to a pre element.
function outf(text) {
    var mypre = document.getElementById("output");
    mypre.innerHTML = mypre.innerHTML + text;
}
function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
        throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

// Here's everything you need to run a python program in skulpt
// grab the code from your textarea
// get a reference to your pre element for output
// configure the output function
// call Sk.importMainWithBody()
function runit() {
    var prog = myeditor.getValue();
    var mypre = document.getElementById("output");
    mypre.innerHTML = '';
    Sk.pre = "output";

    Sk.configure({
        inputfun: function () {
            // the function returns a promise to give a result back later...
            var span = document.createElement('span');
            var input = document.createElement('input');
            input.id = 'active-input';
            span.appendChild(input);
            mypre.appendChild(span);
            input = $('#active-input');
            input.focus();
            return new Promise(function (resolve, reject) {
                input.on("keyup", function (e) {
                    if (e.keyCode == 13) {
                        // remove keyup handler from #output
                        input.off("keyup");
                        // resolve the promise with the value of the input field
                        input.prop('readonly', true);
                        input.id = 'inactive-input';
                        resolve('\n' + input.val() + '\n' + input.val());
                        input.remove();
                    }
                })
            })
        },
        output: outf,
        read: builtinRead,
        __future__: Sk.python3,
    });
    (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'mycanvas';
    var myPromise = Sk.misceval.asyncToPromise(function () {
        return Sk.importMainWithBody("<stdin>", false, prog, true);
    });
    myPromise.then(function (mod) {
        console.log('success');
    },
        function (err) {
            document.getElementById('output').innerHTML += err.toString();
        });
}

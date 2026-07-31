let editor = document.querySelector('#editor')
ace.require("ace/ext/language_tools");
let myeditor = ace.edit(editor, {
    theme: 'ace/theme/dracula',
    mode: 'ace/mode/python',

    enableSnippets: true,
    enableLiveAutocompletion: true
})

// ##############################################
// download terminl
function download_terminal() {
    var text = document.getElementById('output').innerHTML;

    // ایجاد یک شیء Blob با متن وارد شده توسط کاربر
    var blob = new Blob([text], { type: 'text/plain' });

    // ساخت یک لینک برای دانلود فایل
    var a = document.createElement('a');
    a.href = window.URL.createObjectURL(blob);

    // تنظیم نام فایل
    a.download = 'CodenaOutputTerminal.txt';

    // افزودن لینک به صفحه و کلیک بر روی آن
    document.body.appendChild(a);
    a.click();

    // حذف لینک ایجاد شده بعد از دانلود
    window.URL.revokeObjectURL(a.href);

    // حذف لینک از صفحه
    document.body.removeChild(a);
    alertify.success('ترمینال با موفقیت دانلود شد.');
}


// download terminal
// ##########################################




// ##############################################
// download source
function download_file() {
    var text = myeditor.getValue();


    // ایجاد یک شیء Blob با متن وارد شده توسط کاربر
    var blob = new Blob([text], { type: 'text/plain' });

    // ساخت یک لینک برای دانلود فایل
    var a = document.createElement('a');
    a.href = window.URL.createObjectURL(blob);

    // تنظیم نام فایل
    a.download = 'codna-editor.py';

    // افزودن لینک به صفحه و کلیک بر روی آن
    document.body.appendChild(a);
    a.click();

    // حذف لینک ایجاد شده بعد از دانلود
    window.URL.revokeObjectURL(a.href);

    // حذف لینک از صفحه
    document.body.removeChild(a);
    alertify.success("فایل با موفقیت دانلود شد");
}


// download source
// ##########################################


// upload source 
// ###############################
// function upload_file(){
document.getElementById('openFileButton').addEventListener('click', function () {
    // باز کردن پنجره انتخاب فایل
    document.getElementById('fileInput').click();
});

// افزودن رویداد تغییر به ورودی فایل
document.getElementById('fileInput').addEventListener('change', function () {
    var fileInput = document.getElementById('fileInput');


    // بررسی آیا کاربر فایلی انتخاب کرده است
    if (fileInput.files.length > 0) {
        var selectedFile = fileInput.files[0];

        // خواندن محتوای فایل
        var reader = new FileReader();

        reader.onload = function (event) {
            // نمایش محتوای فایل در صفحه
            myeditor.setValue(event.target.result);
            alertify.success("فایل با موفقیت اپلود شد.");
        };

        // خواندن فایل به عنوان متن
        reader.readAsText(selectedFile);
    } else {
        alertify.error("هیچ فایلی انتخاب نشده است.");
    }
});

// }

// upload source 
// ###############################


var rows = myeditor.getValue().split('\n');

function updateRows() {
    rows = myeditor.getValue().split('\n');
    var row_number_pane = document.querySelector('.row-number-pane');
    row_number_pane.innerHTML = '';
    for (var i = 0; i < rows.length; i++) {
        var row = document.createElement('div');
        row.className = 'code-row-number';
        row.id = 'row-' + String(i + 1);
        row.innerHTML = String(i + 1);
        row_number_pane.appendChild(row);
    }
}

const toggleNave = document.getElementById('toggleNave');
const closeNav = document.getElementById('closeNav')
const nav = document.querySelector('.container-2:nth-child(2)')
let isShowNave = false;

if (toggleNave) {
    toggleNave.addEventListener('click', () => {
        if (isShowNave) {
            closeNavFunc()
        } else {
            nav.style.right = '0'
            isShowNave = true
        }
    })
}

if (closeNav) {
    closeNav.addEventListener('click', closeNavFunc)
}

function closeNavFunc() {
    nav.style.right = '-333px'
    isShowNave = false;
}

// #################
// save in server
$(document).ready(function () {
    $('#saveButton').click(function () {
        var inputValue = myeditor.getValue();
        var csrfToken = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            url: "python/save_data/",  // URL ایجاد شده برای ذخیره داده
            method: 'POST',
            data: {
                input_value: inputValue,
                csrfmiddlewaretoken: csrfToken  // اضافه کردن توکن CSRF
            },
            success: function (data) {
                // در اینجا می توانید عملیات پس از موفقیتی انجام داده و پیام خروجی را نمایش دهید.
                alertify.success('عملیات ذخیره سازی با موفقیت انجام شد.');
            },
            error: function (xhr, status, error) {
                // در صورت بروز خطا، اقدامات لازم را انجام دهید.
                alertify.error('خطا در ارسال اطلاعات به سرور: ' + error);
            }
        });
    });
});
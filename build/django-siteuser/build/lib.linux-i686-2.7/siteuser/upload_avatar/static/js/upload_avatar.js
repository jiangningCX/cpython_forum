/*jslint browser: true*/
/*global $*/
"use strict";

$(function () {
    var img_obj, p, fileanme, x1, y1, x2, y2;

    $('#uploadAvatarInputFile').change(function () {
        if ($(this).val() === "") { return; }
        var $last_img = $('#uploadAvatarSelectArea img');
        if ($last_img.length) {
            img_obj = $last_img.imgAreaSelect({instance: true});
            img_obj.remove();
        }
        $('#uploadAvatarSelectArea').empty();
        $('#uploadAvatarPreviewArea div').empty();
        p = new RegExp(/\.(jpg|jpeg|png|gif)$/);
        fileanme = $(this).val().toLowerCase().replace(/^\s+|\s+$/g, '');
        if (!p.test(fileanme)) { window.alert("请选择图片上传"); return; }
        $('#uploadAvatarForm').submit();
        $(this).val('');
        $('#uploadAvatarCropSubmit').removeAttr('disabled');
    });

    $('#uploadAvatarCropSubmit').click(function () {
        $(this).attr('disabled', 'disabled');
        x1 = $('#uploadAvatarValueX1').val();
        y1 = $('#uploadAvatarValueY1').val();
        x2 = $('#uploadAvatarValueX2').val();
        y2 = $('#uploadAvatarValueY2').val();
        if (x1 === "" || y1 === "" || x2 === "" || y2 === "") {
            $(this).removeAttr('disabled');
            return false;
        }

        $('#uploadAvatarCropForm').submit();
        $('#uploadAvatarValueX1').val('');
        $('#uploadAvatarValueY1').val('');
        $('#uploadAvatarValueX2').val('');
        $('#uploadAvatarValueY2').val('');

        $(this).removeAttr('disabled');
        return false;
    });
});

function upload_avatar_error(msg) {
    $("#uploadAvatarCropResult").hide(100).removeClass('alert-success').addClass('alert-error').text(msg).show(200);
}

function crop_avatar_success(msg) {
    $("#uploadAvatarCropResult").hide(100).removeClass('alert-error').addClass('alert-success').text(msg).show(200);
}

function updatePreview50(img, selection) {
    if (parseInt(selection.width, 10) > 0) {
        var ratiox = 50 / selection.width;
        $("#uploadAvatarPreviewArea50 img").css({
            width: Math.round(ratiox * img.width) + 'px',
            marginLeft: '-' + Math.round(ratiox * selection.x1) + 'px',
            marginTop: '-' + Math.round(ratiox * selection.y1) + 'px'
        });
    }
}

function updatePreview120(img, selection) {
    if (parseInt(selection.width, 10) > 0) {
        var ratiox = 120 / selection.width;
        $("#uploadAvatarPreviewArea120 img").css({
            width: Math.round(ratiox * img.width) + 'px',
            marginLeft: '-' + Math.round(ratiox * selection.x1) + 'px',
            marginTop: '-' + Math.round(ratiox * selection.y1) + 'px'
        });
    }
}

function updateCoors(img, selection) {
    $("#uploadAvatarValueX1").val(selection.x1);
    $("#uploadAvatarValueY1").val(selection.y1);
    $("#uploadAvatarValueX2").val(selection.x2);
    $("#uploadAvatarValueY2").val(selection.y2);
    updatePreview50(img, selection);
    updatePreview120(img, selection);
}



function upload_avatar_success(image_url) {
    $('#uploadAvatarSelectArea').empty();
    $('#uploadAvatarPreviewArea div').empty();
    $('#uploadAvatarPreviewArea div').append('<img />');
    $('#uploadAvatarPreviewArea div img').attr('src', image_url).css('max-width', 'none');

    $('#uploadAvatarSelectArea').append('<img />');
    $('#uploadAvatarSelectArea img').attr('src', image_url).load(function () {
        $(this).unbind('load');

        var img_width, img_height, sel, crop_image_area_size = 300;
        img_width = $(this).width();
        img_height = $(this).height();

        if (img_width > crop_image_area_size || img_height > crop_image_area_size) {
            if (img_width >= img_height) {
                $(this).css('width', crop_image_area_size + "px");
            } else {
                $(this).css('height', crop_image_area_size + "px");
            }
        }

        img_width = $(this).width();
        img_height = $(this).height();

        sel = {};
        sel.x1 = Math.round(img_width / 2 - 25 > 0 ? img_width / 2 - 25 : 0);
        sel.y1 = Math.round(img_height / 2 - 25 > 0 ? img_height / 2 - 25 : 0);
        sel.x2 = Math.round(img_width / 2 + 25 > img_width ? img_width : img_width / 2 + 25);
        sel.y2 = Math.round(img_height / 2 + 25 > img_height ? img_height : img_height / 2 + 25);
        sel.width = 50;

        $(this).imgAreaSelect({
            handles: true,
            aspectRatio: "1:1",
            fadeSpeed: 100,
            minHeight: 50,
            minWidth: 50,
            x1: sel.x1,
            y1: sel.y1,
            x2: sel.x2,
            y2: sel.y2,
            onSelectChange: updateCoors
        });

        updateCoors({'width': img_width}, sel);
    });
}


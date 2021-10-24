<template>
    <div class="create-page body-content">
        <div class="left-block">
        card area
        </div>
        <div class="right-block">
            <form id="contact-form" class="form-horizontal" role="form">
            <div class="form-group ">
                <div class="col-sm-12">
                <input type="text" class="form-control form-category" id="name" placeholder="NAME" name="name" value="" required>
                </div>
            </div>

            <div class="form-group">
                <div class="col-sm-12">
                    <input type="email" class="form-control form-category" id="email" placeholder="EMAIL" name="email" value="" required>
                </div>
            </div>

                <textarea class="form-control user-detail" rows="10" placeholder="MESSAGE" name="message" required style='font-family: "Yu Gothic medium", "游ゴシック Medium", Yugothic, "游ゴシック体", "ヒラギノ角 Pro W3", sans-serif;'></textarea>
                <a class="button registor" href="share.html" >登録</a>
            </form>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Create'
}
</script>

<style>
.registor{
    position:absolute;
    left:210px
}
.create-page{
    margin-top:66px;
    display: flex;
}
.right-block{
  text-align:center;
  width:40%;
}
.left-block{
  width:60%;
}
.form-horizontal {
  /*float: left;*/
  width: 400px;
  position:relative;
}
.user-detail{
    height:200px;
}
.form-category{
  height:40px;
  margin-bottom:10px;
}
.form-control,
textarea {
  padding-left:7px;
  font-size:20px;
  resize:none;
  width: 500px;
  background-color: #fff;
  color: #312F2F;
  letter-spacing: 1px;
  border-radius:10px;
  border-width:5px;
  outline :none
}
.user-detail{
  padding-top:10px;
}
.send-button {
  margin-top: 15px;
  height: 34px;
  width: 400px;
  overflow: hidden;
  transition: all .2s ease-in-out;
}

.alt-send-button {
  width: 400px;
  height: 34px;
  transition: all .2s ease-in-out;
}

.send-text {
  display: block;
  margin-top: 10px;
  font: 700 12px 'Lato', sans-serif;
  letter-spacing: 2px;
}

.alt-send-button:hover {
  transform: translate3d(0px, -29px, 0px);
}
</style>

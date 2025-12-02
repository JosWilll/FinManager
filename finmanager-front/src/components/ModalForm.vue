<template id="dial">


  <dialog>
    <button class="modal-close" @click="closeDialog()">X</button>
    <header class="modal-head">
      <slot name="head">A default modal's head</slot>
    </header>
    <section class="modal-body">
      <slot name="body">
        <p>A default modal's body. If u see it, something's wrong</p>
        <button @click="closeDialog()">OK</button>
      </slot>
    </section>
  </dialog>

</template>



<script>
export default{
  name: "Modal-form",
  mounted(){
    //this.showDialog();    // Debug
  },
  methods: {
    showDialog(){
      document.getElementById("dial").showModal()
    },
    closeDialog(){
      document.getElementById("dial").close()
    }
  }
}
</script>

<style>
.bg-dim{
  position: fixed;
  width: 100%;
  height: 100%;
  top:0;
  left:0;
  background-color: rgba(0,0,0,0.4);
  z-index: 1;
}


.modal{
  position: center;
  overflow: auto;
  position: fixed;
  width:30%;
  height:30%;
  z-index: 2;
}

.modal-head{
  border-bottom: 1.5px solid black;
}

.modal-body{
  text-align:center;
}

.modal-close{
  text-align: right;
}
</style>

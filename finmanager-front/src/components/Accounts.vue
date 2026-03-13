<template>
  <h1>Accounts menu</h1>
  <p>Here you can create and edit accounts for managing your money</p>
  <div class="form-check mb-3">
    <input type="checkbox" v-model="showHidden" id="showHiddenAccs" class="form-check-input"/>
    <label for="showHiddenAccs" class="form-check-label">Show hidden accounts</label>
  </div>

  <div class="card-container">
    <div v-for="(acc, index) in accounts" :key="acc.id" class="card" v-show="!acc.isHidden || showHidden" v-bind:style="acc.isHidden ? 'background-color:grey;' : '' ">
      <div v-if="edit!=acc.id">
        <div class="acc-name">{{ acc.name }}</div>
        <div class="acc-balance">{{ acc.balance }}</div>
        <div class="container-wrapper">
          <div class="button-group-acc">
            <button class="button-active">Transfer</button>
            <button class="button-active" @click="edit=acc.id; name=acc.name;balance=acc.balance;isHidden=acc.isHidden">Edit</button>
            <button class="button-active" @click="accDel(acc.id)">Delete</button>
          </div>
        </div>
      </div>
      <div v-else>
        <input type="text" v-model="name" placeholder="Account name..." class="form-control mb-2"/>
        <input type="number" v-model="balance" step="0.01" class="form-control mb-2"/>
        <div class="form-check">
          <input type="checkbox" v-model="isHidden" id="isHidden" class="form-check-input"/>
          <label for="isHidden" class="form-check-label">Hidden</label>
        </div>
        <div class="container-wrapper">
          <div class="button-group-acc">
            <button class="button-active" type="submit" @click="accEdit(acc.id, index)">Confirm</button>
            <button class="button-active" type="button" @click="cancelEdit()">Cancel</button>
          </div>
        </div>
      </div>
    </div>

    <div class="card">

      <div v-if="edit!='new'" @click="cancelEdit();edit='new'" 
      style="
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;">
        <h5>New account</h5>
      </div>
    
      <div v-else>
        <input type="text" v-model="name" placeholder="Account name..." class="form-control mb-2"/>
        <input type="number" v-model="balance" step="0.01" class="form-control mb-2"/>
        <div class="form-check">
          <input type="checkbox" v-model="isHidden" id="isHidden" class="form-check-input"/>
          <label for="isHidden" class="form-check-label">Hidden</label>
        </div>
        <div class="container-wrapper">
          <div class="button-group-acc">
            <button class="btn btn-success" @click="newAcc()">Save</button>
            <button class="btn btn-danger" @click="edit=null">Cancel</button>
          </div>
        </div>

      </div>
      
    </div>
  </div>

</template>

<script>
  import axios from 'axios';

  export default{
    name: 'Accounts-item',
    components: {},
    props: {
      accounts: Array
    },
    data(){
      return{
        edit: null,
        name: '',
        balance: 0,
        isHidden: false,
        showHidden: false
      }
    },
    mounted(){
    },
    methods:{
      cancelEdit(){
        this.name = '';
        this.balance = 0;
        this.isHidden = false;
        this.edit = null;
      },
      async newAcc(){
        try{
          const response =
            await axios.post(this.$hostname + '/accounts/', {
              name: this.name,
              balance: this.balance,
              isHidden: this.isHidden,
            });
          const newAccount = response.data;
          this.$emit("accNew", newAccount);
          this.cancelEdit();
        } catch(error){
          console.log(error);
        }
      },
      async accEdit(id, vueId){
        try{
          const response = await axios.patch(this.$hostname + '/accounts/' + id, {
            name: this.name,
            balance: this.balance,
            isHidden: this.isHidden
          });
          const patchedAcc = response.data;
          this.$emit("accEdit", patchedAcc, vueId);
          this.cancelEdit();
        } catch(error){
          console.log(error);
        }
      },
      async accDel(accid){
        try{
          await axios.delete(this.$hostname + '/accounts/' + accid)
          this.$emit("accDel", accid);
        } catch(error){
          console.log(error);
        }
      }
    }
  }

</script>

<style>
.card-container{
  display: grid;
  grid-template-columns: 1fr;
  gap: 1em;
}

.button-group-acc{
  position:absolute;
  bottom:.5em;
  border-radius: 15px;
}

.container-wrapper{
  display: flex;
  justify-content: center;
}

.card{
  padding: 1em;
  overflow:auto;
  width: 20em;
  height: 12em;
  text-align: center;
  background-color:#b5e7a0;
  text-decoration: none;
  color: black;
}

.card:hover{
  color:black;
  text-decoration: none;
}

        @media (min-width: 1024px) {
          .card-container{
            grid-template-columns: repeat(auto-fill, minmax(20em, 1fr));
          }
        }

        .input-field{
          border: 1px solid green;
          border-radius: 6px;
          background-color: transparent;
        }
</style>

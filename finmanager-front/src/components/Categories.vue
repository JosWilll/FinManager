<template>
  <h1>Categories</h1>
  <table class="table table-hover" style="table-layout: fixed; width: 100%;">
    <colgroup>
      <col style="width: 5%;"/>
      <col style="width: 70%;"/>
      <col style="width: 15%;"/>
      <col style="width: 15%;"/>
    </colgroup>
    <thead style="background-color:#86af49 !important; color:white;">
    <tr>
      <th scope="col">Id</th>
      <th scope="col">Name</th>
      <th scope="col">Is expense?</th>
      <th scope="col">Actions</th>
    </tr>
    </thead>
    <tbody>
      <tr v-for="(cat, index) in categories" :key="cat.id" v-bind:class="(cat.isExpense)? 'table-danger' : 'table-success'">
        <th scope="row">{{ index+1 }}</th>
        <td>
          <span v-if="edit!=cat.id">
            {{ cat.title }}
          </span>
          <input v-else v-model="name" style="width: 100%;"/>
        </td>
        <td>
          <span v-if="edit!=cat.id">
            {{ cat.isExpense ? "Expense" : "Income" }}
          </span>
          <div v-else>
            <input v-model="isExpense" type="checkbox" id="isExp"/>
            <label for="isExp">Is expense?</label>
          </div>
        </td>
        <td>
          <div v-if="edit!=cat.id">
            <button class="btn btn-success" @click="edit=(cat.id);name=(cat.title);isExpense=(cat.isExpense)">Edit</button>
            <button class="btn btn-danger" @click="catDel(cat.id)">Delete</button>
          </div>
          <div v-else>
            <button class="btn btn-success" @click="catEdit(cat.id, index)">Save</button>
            <button class="btn btn-danger" @click="cancelEdit">Cancel</button>
          </div>
        </td>
      </tr>
      <tr v-if="edit=='new'" v-bind:class="(isExpense) ? 'table-danger': 'table-success'">
        <td>{{ categories.length + 1 }}</td>
        <td><input v-model="name" placeholder="Category title" style="width: 100%;"/></td>
        <td>
          <input v-model="isExpense" type="checkbox" id="isExp" />
          <label for="isExp">Is expense?</label>
        </td>
        <td>
          <button class="btn btn-success" @click="catNew()">Save</button>
          <button class="btn btn-danger" @click="cancelEdit()">Cancel</button>
        </td>
      </tr>
    
      <tr v-else class="table-primary">
        <td colspan="4" @click="cancelEdit();edit='new'">New category...</td>
      </tr>
    </tbody>
  </table>
  
</template>

<script>
  import axios from 'axios';
  
  export default{
    name: 'Categories-item',
    props: {
      categories: Array
    },
    data(){
      return{
        edit: '',
        name: '',
        isExpense: false,  // Because by default checkbox is off
      }
    },
    methods:{
      cancelEdit(){
        this.edit = '';
        this.name = '';
        this.isExpense = false;
      },
      async catNew(){
        try{
          const response = await axios.post(this.$hostname + '/categories/', {
            title: this.name,
            isExpense: this.isExpense,
          });
          const newCategory = response.data;
          this.$emit("catNew", newCategory);
          this.name = '';
          this.isExpense = false;
          this.edit = '';
        } catch(error){
          console.log(error);
        }
      },
      async catDel(catID){
        try{
          await axios.delete(this.$hostname + '/categories/' + catID + '/delete');
          this.$emit("catDel", catID);
        } catch(error){
          console.log(error);
        }
      },
      async catEdit(catID, vueId){
        try{
          const response = await axios.patch(this.$hostname + '/categories/' + catID, {
            title: this.name,
            isExpense: this.isExpense
          });
          this.$emit("catEdit", response.data, vueId);
          this.cancelEdit();
        } catch(error){
          console.log(error);
        }
      }
    }
  }
</script>

<style>

</style>

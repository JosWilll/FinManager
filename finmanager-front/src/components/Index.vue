<template>
   <h1>Finmanager home</h1>
  <p>Welcome to finmanager web app! Here you can manage your finances by adding transactions to your money accounts.</p>
  <div class="row">
    <div class="col-sm list-group">
      <h4 class="col-sm ">Top expenses</h4>
        <li v-for="(value, key) in context.expensesDescending" :key="key" class="list-group-item">
          <h5 style="float:left;width:50%;">{{key}}</h5>
          <h5 style="float:right;width:50%;text-align: right;">{{value}}</h5>
        </li>
    </div>
    <div class="col-sm list-group">
      <h4 class="col-sm ">Top incomes</h4>
        <li v-for="(value, key) in context.incomesDescending" :key="key" class="list-group-item">
          <h5 style="float:left;width:50%;">{{key}}</h5>
          <h5 style="float:right;width:50%;text-align: right;">{{value}}</h5>
        </li>
    </div>
  </div>

</template>

<script>
import axios from 'axios';

  export default{
    name: "Index-item",
    components: {},
    data(){
        return{
          context: [],
        }
    },
    mounted(){
      axios.get(this.$hostname)
      .then(response =>{
        this.context = response.data
        console.log(this.context.data)
      })
      .catch((error) => {console.log(error)})
    }
  }
</script>
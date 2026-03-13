<template>
  <h1>Transactions</h1>
  <table class="table table-hover">
    <thead style="background-color:#86af49 !important; color:white;">
      <tr>
        <th>Date and time</th>
        <th>Account</th>
        <th>Category</th>
        <th>Sum</th>
        <th>Actions</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(t, index) in transactions" :key="t.id" v-bind:class="(t.isExpense) ? 'table-danger' : 'table-success' ">
        <td>
          <span v-if="edit!=t.id">
            {{ t.tDateTime }}
          </span>
          <input v-else type="datetime-local" v-model="tDateTime" />
        </td>
        <td>
          <span v-if="edit!=t.id">
            {{ accounts.find(a => Number(a.id) === Number(t.account))?.name }}
          </span>
          <select v-else v-model="account">
            <option v-for="acc in accounts" :key="acc.id" :value="acc.id">{{ acc.name }}</option>
          </select>
        </td>
        <td>
          <span v-if="edit!=t.id">
            {{ categories.find(c => c.id === t.category)?.title }}
          </span>
          <div v-else>
            <div style="display: inline;">
              <input type="radio" name="isExpense" value="expense" v-model="isExpense" checked />
              <label for="expense">Expense</label>
              <input type="radio" name="isExpense" value="income" v-model="isExpense" />
              <label for="income">Income</label>
            </div>
            <select v-model="category" v-if="isExpense=='expense'">
              <option v-for="cat in categories.filter(c => c.isExpense)" :key="cat.id" :value="cat.id">{{ cat.title }}</option>
            </select>
            <select v-model="category" v-if="isExpense=='income'">
              <option v-for="cat in categories.filter(c => !c.isExpense)" :key="cat.id" :value="cat.id">{{ cat.title }}</option>
            </select>
          </div>
        </td>
        <td>
          <span v-if="edit!=t.id">
            {{ t.tsum }}
          </span>
          <input v-else type="number" min="0" step="0.01" v-model="tsum"/>
        </td>
        <td>
          <div v-if="edit!=t.id">
            <button class="btn btn-success" @click="editTranForm(t)">Edit</button>
            <button class="btn btn-danger" @click="delTran(t.id)">Delete</button>
          </div>
          <div v-else>
            <button class="btn btn-success" @click="editTran(t.id, index)">Save</button>
            <button class="btn btn-danger" @click="cancelEdit">Cancel</button>
          </div>
        </td>

      </tr>
      <tr class="table-primary" v-if="edit!='new'" @click="cancelEdit();edit='new';tDateTime=getNowTime()">
        <td colspan="5" >New transaction</td>
      </tr>

      <tr v-else class="table-primary">
        <td>
          <input type="datetime-local" v-model="tDateTime" />
        </td>
        <td>
          <select v-model="account">
            <option v-for="acc in accounts" :key="acc.id" :value="acc.id">{{ acc.name }}</option>
          </select>
        </td>
        <td>
          <div style="display: inline;">
            <input type="radio" name="isExpense" value="expense" v-model="isExpense" checked />
            <label for="expense">Expense</label>
            <input type="radio" name="isExpense" value="income" v-model="isExpense" />
            <label for="income">Income</label>
          </div>
          <select v-model="category" v-if="isExpense=='expense'">
            <option v-for="cat in categories.filter(c => c.isExpense)" :key="cat.id" :value="cat.id">{{ cat.title }}</option>
          </select>
          <select v-model="category" v-if="isExpense=='income'">
            <option v-for="cat in categories.filter(c => !c.isExpense)" :key="cat.id" :value="cat.id">{{ cat.title }}</option>
          </select>
        </td>
        <td>
          <input type="number" min="0" step="0.01" v-model="tsum"/>
        </td>
        <td>
          <div>
            <button class="btn btn-success" @click="newTran()">Save</button>
            <button class="btn btn-danger" @click="cancelEdit">Cancel</button>
          </div>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Transactions-item',
  props: {
    transactions: Array,
    categories: Array,
    accounts: Array
  },
  components: {  },
  data() {
    return {
      edit: null,
      displayComment: null,
      tsum: '',
      category: '',
      account: '',
      comment: '',
      isExpense: 'expense',
      checkID: null,
      tDateTime: ''
    }
  },
  methods: {
    getNowTime(){
      let currTime = new Date();
      return currTime.toISOString().slice(0,16);
    },
    cancelEdit(){
      this.edit = null
      this.displayComment = ''
      this.tsum = ''
      this.category = ''
      this.account = ''
      this.comment = ''
      this.isExpense = 'expense'
      this.checkID = null
      this.tDateTime = ''
    },
    editTranForm(tran){
      this.edit = tran.id;
      this.tsum = tran.tsum;
      this.category = tran.category;
      this.account = tran.account;
      this.comment = tran.commen;
      this.checkID = tran.checkID;
      this.tDateTime = tran.tDateTime;
    },
    async newTran() {
      try {
        const response = await axios.post(this.$hostname + '/transactions/', {
          tsum: this.tsum,
          category: this.category,
          account: this.account,
          comment: this.comment,
          isExpense: this.categories.find(c => c.id === this.category)?.isExpense,
          checkID: this.checkID,
          tDateTime: this.tDateTime
        });

        const newTran = response.data;
        this.$emit("tNew", newTran);

        this.cancelEdit();
      } catch (error) {
        console.log(error);
      }
    },
    async editTran(id, vueID){
      try{
        const response = await axios.patch(this.$hostname + '/transactions/' + id, {
          tsum: this.tsum,
          category: this.category,
          account: this.account,
          checkID: this.checkID,
          tDateTime: this.tDateTime,
          comment: this.comment,
          isExpense: this.categories.find(c => c.id === this.category)?.isExpense
        });

        this.$emit(response.data, vueID);

      } catch(error){
        console.log(error);
      }
    },
    async delTran(id){
      try{
        await axios.delete(this.$hostname + '/transactions/' + id + '/delete');
        this.$emit("tDel", id);
      } catch(error){
        console.log(error);
      }
    },
    showComment(id){
      this.displayComment = this.displayComment != id ? id : '';
    }
  }
}
</script>

<style>
.form-group {
  margin: 1em;
}

.form-group label {
  text-align: left;
}

#calc {
  display: none;
}
</style>
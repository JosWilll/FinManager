<template>
    <table>
        <thead>
            <tr>
                <th>Date and time</th>
                <th>Sum</th>
                <th>Category</th>
            </tr>
        </thead>
        <tbody v-for="t in transactions" :key="t.id">
            <tr>
                <th>{{ t.tDateTime }}</th>
                <th>{{ t.tsum }}</th>
                <th>{{ t.category }}</th>
            </tr>
        </tbody>
    </table>

    <modal-form>
        <template v-slot:head>Create a new transaction</template>
        <template v-slot:body>
            <form v-on:submit.prevent="newTran">
                <div class="form-group">
                    <label for="tsum">Transaction sum</label>
                    <input type="text" id="tsum" v-model="tsum">
                </div>
                <div class="form-group">
                    <label for="category">Category</label>
                    <input type="text" id="category" v-model="category">
                </div>
                <div class="form-group">
                    <label for="account">Account</label>
                    <input type="text" id="account" v-model="account">
                </div>
                <div class="form-group">
                    <label for="comment">Comment (optional)</label>
                    <textarea id="comment"></textarea>
                </div>
                <div class="form-group"></div>
                <button type="submit">Confirm</button>
            </form>
            <calculator id="calc"/>
        </template>
    </modal-form>
</template>

<script>
import axios from 'axios';
import ModalForm from './ModalForm.vue';
import calculator from './calculator.vue';

export default{
    name: 'Transactions-item',
    components: {ModalForm, calculator},
    data() {
        return{
            // transactions: [],
            // cats: [],
            // accs: [],
            tsum: '',
            category: '',
            account: '',
            comment: '',
            isExpense: '',
            checkID: '',
            tDateTime: ''
        }
    },
    mounted(){
        // axios.get(this.$hostname + '/transactions')
        // .then((res)=> {
        //     this.transactions = res.data;
        // })
        // .catch((err)=>{console.log(err)})
        
        // axios.get(this.$hostname + '/categories')
        // .then((res)=> {
        //     this.cats = res.data;
        // })
        // .catch((err)=>{console.log(err)})

        // axios.get(this.$hostname + '/accounts')
        // .then((res)=> {
        //     this.accs = res.data;
        // })
        // .catch((err)=>{console.log(err)})
    },
    methods: {
        async newTran(){
            try{
                const response = await axios.post(this.$hostname + '/transactions', {
                    tsum: this.tsum,
                    category: this.category,
                    account: this.account,
                    comment: this.comment,
                    isExpense: this.isExpense,  // Change to fetch with category type
                    checkID: this.checkID,
                    tDateTime: this.tDateTime
                });

                this.transactions.push(response.data);

                this.tsum = '';
                this.category = '';
                this.account = '';
                this.comment = '';
                this.isExpense = '';
                this.checkID = '';
                this.tDateTime = '';

            
            } catch(error){
                console.log(error);
            }
        }
    }
}
</script>

<style>
    .form-group{
        margin: 1em;
    }
    .form-group label{
        text-align: left;
    }
    #calc{
        display: none;
    }
</style>
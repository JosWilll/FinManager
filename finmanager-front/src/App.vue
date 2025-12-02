<template>
				<div>
								<Navbar/>
								<div class="row">
												<div class="col-md-10 container-fluid">
																<div class="m-5">
																				<RouterView class="m-3"
																										:accounts="accounts"
																										:transactions="transactions"
																										:categories="categories"
																										@accNew="accNew"
																										@accEdit="accEdit"
																										@accDel="accDelete"
																										@catNew="catNew"
																										@catEdit="catEdit"
																										@catDel="catDelete"
																										/>
																</div>
												</div>
												<div class="col-md-2 utilities">
																<Sidebar/>
												</div>
								</div>
				</div>
</template>

<script>
				import axios from 'axios';
				import Navbar from './components/Navbar.vue';
				import Sidebar from './components/Sidebar.vue';

				export default {
								name: 'App',
								components: {Navbar, Sidebar},
								data() {
												return {
																transactions: [],
																cats: [],
																accounts: [],
												}
								},
								methods: {
												accNew(newAccount){
																this.accounts.push(newAccount);
												},
												accEdit(patchedAcc, id){
																this.accounts[id] = patchedAcc;
												},
												accDelete(pk){
																this.accounts = this.accounts.filter(acc => acc.id !=pk)
												},
												catNew(cat){
																this.cats.push(cat);
												},
												catEdit(cat, id){
																this.cats[id] = cat;
												},
												catDelete(pk){
																this.cats = this.cats.filter(cat => cat.id != pk)
												},
								},
								mounted(){
												axios.get(this.$hostname + '/transactions')
																.then((res)=> {
																				this.transactions = res.data;
																})
																.catch((err)=>{console.log(err)})

												axios.get(this.$hostname + '/categories')
																.then((res)=> {
																				this.cats = res.data;
																})
																.catch((err)=>{console.log(err)})

												axios.get(this.$hostname + '/accounts')
																.then((res)=> {
																				this.accounts = res.data;
																})
																.catch((err)=>{console.log(err)})
								},
				}
</script>

<style>
#app {
				font-family: Arial, Helvetica, sans-serif;

}

body{
				background-image: linear-gradient(
								135deg,
								white 0%,
								#86af49 100%
								);
}

.button-group{
				border-radius: 25px;
}

.button-active{
				background-color: #86af49;
				border:none;
				color: white;
				padding-left: 0.75rem;
				padding-right: 0.75rem;
				padding-top: 0.375rem; 
				padding-bottom: 0.375rem; 
				text-align: center; 
				transition: 0.3s;
}

.button-active:hover{
				background-color: #648337;
				color:white;
				text-decoration: none;}

.utilities {
				background-color: #f1f3f5;
				padding: 15px;
				height: 100vh;
}
</style>

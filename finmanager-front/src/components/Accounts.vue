<template>
				<h1>Accounts menu</h1>
				<p>Here you can create and edit accounts for managing your money</p>

				<div class="card-container">
								<div v-for="(acc, index) in accounts" :key="acc.id" class="card">
												<div v-if="showForm!=acc.id">
																<div class="acc-name">{{ acc.name }}</div>
																<div class="acc-balance">{{ acc.balance }}</div>
																<div class="container-wrapper">
																				<div class="button-group-acc">
																								<button class="button-active">Transfer</button>
																								<button class="button-active" @click="accEditForm(acc.id, acc.name, acc.balance, false)">Edit</button>
																								<button class="button-active" @click="accDel(acc.id)">Delete</button>
																				</div>
																</div>
												</div>
												<div v-else>
																<form v-on:submit.prevent="accEdit(acc.id, index)">
																				<div class="acc-name form-group">
																								<input type="text" class="input-field" id="name" v-model="name" placeholder="Account name...">
																				</div>
																				<div class="acc-balabce form-group">
																								<input type="text" class="input-field" id="balance" v-model="balance" placeholder="Balance..." value="0">
																				</div>
																				<div class="form-group">
																								<label for="isHidden">Is account hidden </label>
																								<input type="checkbox" id="isHidden" v-model="isHidden">
																				</div>
																				<div class="container-wrapper">
																								<div class="button-group-acc">
																												<button class="button-active" @click="clearHide()">Cancel</button>
																												<button class="button-active" type="submit">Confirm</button>
																								</div>
																				</div>

																</form>
												</div>
								</div>

								<a class="card" id="newAccButton" @click="showForm='new'" v-show="showForm!='new'">

												<div>
																<h3 style="text-align: center;margin-bottom: 0em;">+</h3>
																<h5 style="text-align: center;margin-bottom: 0em;">New account</h5>
												</div>
								</a>
								<div class="card" id="newAcc" v-show="showForm=='new'">
												<form v-on:submit.prevent="newAcc">
																<div class="acc-name form-group">
																				<input type="text" class="input-field" id="name" v-model="name" placeholder="Account name...">
																</div>
																<div class="acc-balabce form-group">
																				<input type="text" class="input-field" id="balance" v-model="balance" placeholder="Balance..." value="0">
																</div>
																<div class="form-group">
																				<label for="isHidden">Is account hidden </label>
																				<input type="checkbox" id="isHidden" v-model="isHidden">
																</div>
																<div class="container-wrapper">
																				<div class="button-group-acc">
																								<button class="button-active" @click="clearHide()">Cancel</button>
																								<button class="button-active" type="submit">Confirm</button>
																				</div>
																</div>
												</form>
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
																showForm: false,
																name: '',
																balance: '',
																isHidden: ''
												}

								},
								mounted(){
								},
								methods:{
												accEditForm(id, name, bal, hidden){
																this.showForm = id;
																this.name = name;
																this.balance = bal;
																this.isHidden = hidden;
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
																				this.name = '';
																				this.balance = '';
																				this.isHidden = '';

																				this.showForm = false;

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

												},
												clearHide(){
																this.name = '';
																this.balance = '';
																this.isHidden = '';
																this.showForm = false;
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

																				this.name = '';
																				this.balance = '';
																				this.isHidden = '';

																				this.showForm = false;
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
				height: 10em;
				text-align: center;
				background-color:#b5e7a0;
				text-decoration: none;
				color: black;
}

.card:hover{
				color:black;
				text-decoration: none;
}

			/*
				 .acc-name{
								 border-bottom: 1.5px solid black;
				 }
			 */
				 @media (min-width: 1024px) {
								 .card-container{
												 /*grid-template-columns: 1fr 1fr 1fr 1fr;*/
												 grid-template-columns: repeat(auto-fill, minmax(20em, 1fr));
								 }
				 }

				 .input-field{
								 border: 1px solid green;
								 border-radius: 6px;
								 background-color: transparent;
				 }
</style>

<template>
  <div id="topnav" class="topnav">
    <div class="btn-group">
      <router-link to="/" class="button-active">
        Home
      </router-link>
      <router-link to="/transactions" class="button-active">
        Transactions
      </router-link>
      <router-link to="/categories" class="button-active">
        Categories
      </router-link>
      <router-link to="/accounts" class="button-active">
        Accounts
      </router-link>
    </div>
  </div>
</template>

<script>
  export default{
    name: "Navbar-item"
  }
</script>

<style>
.topnav{
      background-color: #86af49;
      overflow: hidden;
}

.topnav-button{
  background-color: #86af49;
  color: white;
  padding-left: 0.75rem;
  padding-right: 0.75rem;
  padding-top: 0.375rem;
  padding-bottom: 0.375rem;
  text-align: center;
  transition: 0.3s;
}

.topnav-button:hover{
  background-color: #648337;
  color:white;
  text-decoration: none;
}
</style>
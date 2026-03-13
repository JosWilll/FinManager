<template>
<aside>
            <h5>Quick Actions</h5>
            <hr>

            <h6>Stats</h6>

            <p>Current balance: </p>
            <p>Expenses this month: </p>
            <p>Incomes this month: </p>
            <canvas id="chartExpContainer"></canvas>
            <canvas id="chartIncContainer"></canvas>
            <h6>Calculator</h6>
            <Calculator/>


      </aside>
</template>

<script>
import Calculator from './calculator.vue';

export default{
    name: 'sidebar-item',
    components: {Calculator}
}

</script>


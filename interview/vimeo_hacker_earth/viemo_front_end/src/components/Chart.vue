<template>
    <div id="search">
        <h3> Chart Page</h3>
        <div>
            <el-table
                    :data="bankAccountLists"
                    height="450"
                    style="width: 100%">
                <el-table-column
                        prop="Account No"
                        label="Account No"
                        width="180">
                </el-table-column>
                <el-table-column
                        prop="Date"
                        label="Date"
                        width="180">
                </el-table-column>
                <el-table-column
                        prop="Transaction Details"
                        label="Transaction Details">
                </el-table-column>
                <el-table-column
                        prop="Withdrawal AMT"
                        label="Withdrawal AMT">
                </el-table-column>
                <el-table-column
                        prop="Deposit AMT"
                        label="Deposit AMT">
                </el-table-column>
                <el-table-column
                        prop="Balance AMT"
                        label="Balance AMT">
                </el-table-column>
            </el-table>
            <div class="pagination-wrapper">
                <el-pagination
                        background
                        layout="prev, pager, next"
                        :total=total
                        @current-change="currentPageChanged($event)">
                </el-pagination>
            </div>
        </div>
    </div>
</template>

<script>
    import {mapGetters} from 'vuex'
    export default {
        name: 'Chart',
        components: {

        },
        data(){
            return {
                per_page: 10,
                bankAccountLists: [],
                columns:[],
                formOptions:{},
                allbankAccountLists:[],
                total:0
            }
        },
        created() {
            this.fetchAllAccounts()
        },
        watch:{
            getBankAccountList: function(newVal, oldVal){
                this.allbankAccountLists = newVal
                this.bankAccountLists = newVal
                this.total = newVal.length
            }
        },
        computed:{
            ...mapGetters({getBankAccountList:'getBankAccountList'})
        },
        methods:{
            fetchAllAccounts(){
                this.$store.dispatch('FETCH_ALL_ACCOUNTS', this.page)
            },
            currentPageChanged(id){
                let start = ((id-1) * this.per_page)
                let end = (id * this.per_page)
                this.bankAccountLists = this.allbankAccountLists.slice(start, end)
            }
        }
    }
</script>

<style scoped="css">
</style>

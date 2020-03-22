<template>
    <div id="search">
        <h3> Search Page</h3>
        <div>
            <el-container align="right">
                <el-header>
                    <el-input v-model="search"  size="mini"
                              placeholder="Type to search" @input="searchtext"/>
                </el-header>
            </el-container>
            <el-table
                    :data="bankAccountLists"
                    height="450"
                    style="width: 100%"
                    :default-sort = "{prop: 'Date', order: 'descending'}">
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
        name: 'search',
        components: {

        },
        data(){
            return {
                per_page: 10,
                bankAccountLists: [],
                columns:[],
                formOptions:{},
                allbankAccountLists:[],
                total:0,
                search:''
            }
        },
        created() {
            this.fetchAllAccounts()
        },
        watch:{
            getBankAccountList: function(newVal, oldVal){
                this.allbankAccountLists = newVal
                this.bankAccountLists = newVal.slice(0, 10)
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
            },
            searchtext(){
                let text = this.search
                console.log(text)

                let d = []
                if(text !== ''){
                    if(text.length < 4){
                        return false
                    }
                     d = this.allbankAccountLists.filter(data => !text || data['Transaction Details'].toLowerCase().includes(text.toLowerCase()))
                    this.total = d.length
                     d = d.slice(0,10)

                }else{
                    d = this.allbankAccountLists.slice(0, 10)
                    this.total = this.allbankAccountLists.length
                }
                console.log(d)
                this.bankAccountLists = d
            }
        }
    }
</script>

<style scoped="css">
</style>

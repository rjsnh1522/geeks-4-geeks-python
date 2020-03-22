import http from '@/utils/http-common'

export default class SearchApi {
    static get_bank_accounts(params) {
        return http.get('/bankAccount')
    }
    static get_bank_account(id) {
        return http.get('/bankAccount' + id + '/')
    }
}

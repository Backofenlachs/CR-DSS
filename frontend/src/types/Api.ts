
export default interface ApiResponse<T>{
    meta: ApiMeta
    data: T
}

export interface ApiMeta {
    success: boolean;
    timestamp: string;
}


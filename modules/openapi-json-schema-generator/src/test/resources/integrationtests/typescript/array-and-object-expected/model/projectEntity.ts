/**
 * Cupix API
 * No description provided (generated by Openapi Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)
 *
 * The version of the OpenAPI document: 1.7.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */
import { ProjectEntityLocation } from './projectEntityLocation';


export interface ProjectEntity { 
    id: number;
    kind?: ProjectEntity.KindEnum;
    thumbnail_url?: string;
    name?: string;
    state?: string;
    meta?: object;
    location?: ProjectEntityLocation;
    created_at?: string;
    updated_at?: string;
    published_at?: string;
}
export namespace ProjectEntity {
    export type KindEnum = 'project';
    export const KindEnum = {
        Project: 'project' as KindEnum
    };
}



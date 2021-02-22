/*
 * Kadaster - BRK-Bevragen API
 * D.m.v. deze toepassing worden meerdere, korte bevragingen op de Basis Registratie Kadaster beschikbaar gesteld. Deze toepassing betreft het verstrekken van Kadastrale Onroerende Zaak informatie. 
 *
 * The version of the OpenAPI document: 1.2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.model;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.openapitools.client.model.BeslagHal;

/**
 * BeslagHalCollectieEmbedded
 */
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2021-02-22T09:44:54.145Z[Etc/UTC]")
public class BeslagHalCollectieEmbedded {
  public static final String SERIALIZED_NAME_BESLAGEN = "beslagen";
  @SerializedName(SERIALIZED_NAME_BESLAGEN)
  private List<BeslagHal> beslagen = null;


  public BeslagHalCollectieEmbedded beslagen(List<BeslagHal> beslagen) {
    
    this.beslagen = beslagen;
    return this;
  }

  public BeslagHalCollectieEmbedded addBeslagenItem(BeslagHal beslagenItem) {
    if (this.beslagen == null) {
      this.beslagen = new ArrayList<>();
    }
    this.beslagen.add(beslagenItem);
    return this;
  }

   /**
   * Get beslagen
   * @return beslagen
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public List<BeslagHal> getBeslagen() {
    return beslagen;
  }


  public void setBeslagen(List<BeslagHal> beslagen) {
    this.beslagen = beslagen;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    BeslagHalCollectieEmbedded beslagHalCollectieEmbedded = (BeslagHalCollectieEmbedded) o;
    return Objects.equals(this.beslagen, beslagHalCollectieEmbedded.beslagen);
  }

  @Override
  public int hashCode() {
    return Objects.hash(beslagen);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class BeslagHalCollectieEmbedded {\n");
    sb.append("    beslagen: ").append(toIndentedString(beslagen)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}


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
import org.openapitools.client.model.Waardelijst;

/**
 * Waardelijst in deze component :   [aard](http://www.kadaster.nl/schemas/waardelijsten/AardAantekening/) 
 */
@ApiModel(description = "Waardelijst in deze component :   [aard](http://www.kadaster.nl/schemas/waardelijsten/AardAantekening/) ")
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.JavaClientCodegen", date = "2021-02-22T09:44:54.145Z[Etc/UTC]")
public class AantekeningBasis {
  public static final String SERIALIZED_NAME_AARD = "aard";
  @SerializedName(SERIALIZED_NAME_AARD)
  private Waardelijst aard;

  public static final String SERIALIZED_NAME_OMSCHRIJVING = "omschrijving";
  @SerializedName(SERIALIZED_NAME_OMSCHRIJVING)
  private String omschrijving;

  public static final String SERIALIZED_NAME_BETREFT_GEDEELTE_VAN_PERCEEL = "betreftGedeelteVanPerceel";
  @SerializedName(SERIALIZED_NAME_BETREFT_GEDEELTE_VAN_PERCEEL)
  private Boolean betreftGedeelteVanPerceel;


  public AantekeningBasis aard(Waardelijst aard) {
    
    this.aard = aard;
    return this;
  }

   /**
   * Get aard
   * @return aard
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Waardelijst getAard() {
    return aard;
  }


  public void setAard(Waardelijst aard) {
    this.aard = aard;
  }


  public AantekeningBasis omschrijving(String omschrijving) {
    
    this.omschrijving = omschrijving;
    return this;
  }

   /**
   * Get omschrijving
   * @return omschrijving
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public String getOmschrijving() {
    return omschrijving;
  }


  public void setOmschrijving(String omschrijving) {
    this.omschrijving = omschrijving;
  }


  public AantekeningBasis betreftGedeelteVanPerceel(Boolean betreftGedeelteVanPerceel) {
    
    this.betreftGedeelteVanPerceel = betreftGedeelteVanPerceel;
    return this;
  }

   /**
   * Get betreftGedeelteVanPerceel
   * @return betreftGedeelteVanPerceel
  **/
  @javax.annotation.Nullable
  @ApiModelProperty(value = "")

  public Boolean getBetreftGedeelteVanPerceel() {
    return betreftGedeelteVanPerceel;
  }


  public void setBetreftGedeelteVanPerceel(Boolean betreftGedeelteVanPerceel) {
    this.betreftGedeelteVanPerceel = betreftGedeelteVanPerceel;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    AantekeningBasis aantekeningBasis = (AantekeningBasis) o;
    return Objects.equals(this.aard, aantekeningBasis.aard) &&
        Objects.equals(this.omschrijving, aantekeningBasis.omschrijving) &&
        Objects.equals(this.betreftGedeelteVanPerceel, aantekeningBasis.betreftGedeelteVanPerceel);
  }

  @Override
  public int hashCode() {
    return Objects.hash(aard, omschrijving, betreftGedeelteVanPerceel);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class AantekeningBasis {\n");
    sb.append("    aard: ").append(toIndentedString(aard)).append("\n");
    sb.append("    omschrijving: ").append(toIndentedString(omschrijving)).append("\n");
    sb.append("    betreftGedeelteVanPerceel: ").append(toIndentedString(betreftGedeelteVanPerceel)).append("\n");
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


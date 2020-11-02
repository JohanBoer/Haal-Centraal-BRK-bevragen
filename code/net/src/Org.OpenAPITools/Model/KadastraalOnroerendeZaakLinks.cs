/* 
 * Kadaster - BRK-Bevragen API
 *
 * D.m.v. deze toepassing worden meerdere, korte bevragingen op de Basis Registratie Kadaster beschikbaar gesteld. Deze toepassing betreft het verstrekken van Kadastrale Onroerende Zaak informatie. 
 *
 * The version of the OpenAPI document: 1.2.0
 * 
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// KadastraalOnroerendeZaakLinks
    /// </summary>
    [DataContract]
    public partial class KadastraalOnroerendeZaakLinks :  IEquatable<KadastraalOnroerendeZaakLinks>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="KadastraalOnroerendeZaakLinks" /> class.
        /// </summary>
        /// <param name="self">self.</param>
        /// <param name="zakelijkGerechtigden">zakelijkGerechtigden.</param>
        /// <param name="privaatrechtelijkeBeperkingen">privaatrechtelijkeBeperkingen.</param>
        /// <param name="hypotheken">hypotheken.</param>
        /// <param name="beslagen">beslagen.</param>
        public KadastraalOnroerendeZaakLinks(HalLink self = default(HalLink), List<HalLink> zakelijkGerechtigden = default(List<HalLink>), List<HalLink> privaatrechtelijkeBeperkingen = default(List<HalLink>), List<HalLink> hypotheken = default(List<HalLink>), List<HalLink> beslagen = default(List<HalLink>))
        {
            this.Self = self;
            this.ZakelijkGerechtigden = zakelijkGerechtigden;
            this.PrivaatrechtelijkeBeperkingen = privaatrechtelijkeBeperkingen;
            this.Hypotheken = hypotheken;
            this.Beslagen = beslagen;
        }
        
        /// <summary>
        /// Gets or Sets Self
        /// </summary>
        [DataMember(Name="self", EmitDefaultValue=false)]
        public HalLink Self { get; set; }

        /// <summary>
        /// Gets or Sets ZakelijkGerechtigden
        /// </summary>
        [DataMember(Name="zakelijkGerechtigden", EmitDefaultValue=false)]
        public List<HalLink> ZakelijkGerechtigden { get; set; }

        /// <summary>
        /// Gets or Sets PrivaatrechtelijkeBeperkingen
        /// </summary>
        [DataMember(Name="privaatrechtelijkeBeperkingen", EmitDefaultValue=false)]
        public List<HalLink> PrivaatrechtelijkeBeperkingen { get; set; }

        /// <summary>
        /// Gets or Sets Hypotheken
        /// </summary>
        [DataMember(Name="hypotheken", EmitDefaultValue=false)]
        public List<HalLink> Hypotheken { get; set; }

        /// <summary>
        /// Gets or Sets Beslagen
        /// </summary>
        [DataMember(Name="beslagen", EmitDefaultValue=false)]
        public List<HalLink> Beslagen { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class KadastraalOnroerendeZaakLinks {\n");
            sb.Append("  Self: ").Append(Self).Append("\n");
            sb.Append("  ZakelijkGerechtigden: ").Append(ZakelijkGerechtigden).Append("\n");
            sb.Append("  PrivaatrechtelijkeBeperkingen: ").Append(PrivaatrechtelijkeBeperkingen).Append("\n");
            sb.Append("  Hypotheken: ").Append(Hypotheken).Append("\n");
            sb.Append("  Beslagen: ").Append(Beslagen).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as KadastraalOnroerendeZaakLinks);
        }

        /// <summary>
        /// Returns true if KadastraalOnroerendeZaakLinks instances are equal
        /// </summary>
        /// <param name="input">Instance of KadastraalOnroerendeZaakLinks to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(KadastraalOnroerendeZaakLinks input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Self == input.Self ||
                    (this.Self != null &&
                    this.Self.Equals(input.Self))
                ) && 
                (
                    this.ZakelijkGerechtigden == input.ZakelijkGerechtigden ||
                    this.ZakelijkGerechtigden != null &&
                    input.ZakelijkGerechtigden != null &&
                    this.ZakelijkGerechtigden.SequenceEqual(input.ZakelijkGerechtigden)
                ) && 
                (
                    this.PrivaatrechtelijkeBeperkingen == input.PrivaatrechtelijkeBeperkingen ||
                    this.PrivaatrechtelijkeBeperkingen != null &&
                    input.PrivaatrechtelijkeBeperkingen != null &&
                    this.PrivaatrechtelijkeBeperkingen.SequenceEqual(input.PrivaatrechtelijkeBeperkingen)
                ) && 
                (
                    this.Hypotheken == input.Hypotheken ||
                    this.Hypotheken != null &&
                    input.Hypotheken != null &&
                    this.Hypotheken.SequenceEqual(input.Hypotheken)
                ) && 
                (
                    this.Beslagen == input.Beslagen ||
                    this.Beslagen != null &&
                    input.Beslagen != null &&
                    this.Beslagen.SequenceEqual(input.Beslagen)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Self != null)
                    hashCode = hashCode * 59 + this.Self.GetHashCode();
                if (this.ZakelijkGerechtigden != null)
                    hashCode = hashCode * 59 + this.ZakelijkGerechtigden.GetHashCode();
                if (this.PrivaatrechtelijkeBeperkingen != null)
                    hashCode = hashCode * 59 + this.PrivaatrechtelijkeBeperkingen.GetHashCode();
                if (this.Hypotheken != null)
                    hashCode = hashCode * 59 + this.Hypotheken.GetHashCode();
                if (this.Beslagen != null)
                    hashCode = hashCode * 59 + this.Beslagen.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}
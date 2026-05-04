import {
  S3Client,
  PutObjectCommand,
  GetObjectCommand,
  DeleteObjectCommand,
} from "@aws-sdk/client-s3";
import { getSignedUrl } from "@aws-sdk/s3-request-presigner";

const s3Client = new S3Client({
  region: "auto",
  endpoint: process.env.S3_ENDPOINT,
  credentials: {
    accessKeyId: process.env.S3_ACCESS_KEY || "",
    secretAccessKey: process.env.S3_SECRET_KEY || "",
  },
});

export const uploadDocument = async (
  key: string,
  body: Buffer,
  contentType: string
) => {
  const command = new PutObjectCommand({
    Bucket: process.env.S3_BUCKET,
    Key: key,
    Body: body,
    ContentType: contentType,
  });

  try {
    await s3Client.send(command);
    return { success: true, key };
  } catch (error) {
    console.error("S3 upload error:", error);
    throw error;
  }
};

export const getDocumentUrl = async (key: string, expiresIn = 3600) => {
  const command = new GetObjectCommand({
    Bucket: process.env.S3_BUCKET,
    Key: key,
  });

  try {
    const url = await getSignedUrl(s3Client, command, {
      expiresIn,
    });
    return url;
  } catch (error) {
    console.error("S3 URL generation error:", error);
    throw error;
  }
};

export const deleteDocument = async (key: string) => {
  const command = new DeleteObjectCommand({
    Bucket: process.env.S3_BUCKET,
    Key: key,
  });

  try {
    await s3Client.send(command);
    return { success: true };
  } catch (error) {
    console.error("S3 delete error:", error);
    throw error;
  }
};
